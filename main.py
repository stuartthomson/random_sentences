import pickle
from random import choice
from typing import Dict, List

from language_tool_python import LanguageTool
# from language_tool_python.server import LanguageToolPublicAPI
from language_tool_python.utils import correct

from qrng import get_branch_number
from sentence_scrambler import SentenceScrambler
from word import Sentence
from tweeter import tweet
from blackletter import to_blackletter
from typing import NamedTuple

# TODO: I need java!
tool = LanguageTool('en-GB')
# tool = LanguageToolPublicAPI('en-GB')

WORDS_DICT: Dict[str, List[str]] = pickle.load(open('./ascii_words.pickle', 'rb'))
SENTENCES: List[Sentence] = pickle.load(open('./sentences.pickle', 'rb'))

def correct_sentence(tool: LanguageTool, sentence: str) -> str:
    matches = tool.check(sentence)
    # Example from https://pypi.org/project/language-tool-python/
    filtered_matches = [m for m in matches if m.ruleId != 'MORFOLOGIK_RULE_EN_GB']
    return correct(sentence, filtered_matches)

class SentenceRepresentations(NamedTuple):
    normal: str
    blackletter: str

def create_sentence() -> SentenceRepresentations:
    while True:
        sentence = choice(SENTENCES)
        scrambler = SentenceScrambler(sentence, word_dict=WORDS_DICT)
        new_sentence = scrambler.scramble()
        if len(new_sentence) <= 140:
            corrected = correct_sentence(tool, new_sentence)
            if len(corrected) <= 140:
                try:
                    return SentenceRepresentations(
                        normal=corrected,
                        blackletter=to_blackletter(corrected)
                    )
                except Exception as err:
                    print(f'Warning: {err}')
                    pass

if __name__ == "__main__":
    import sys
    import string
    # with open('blackletter.txt', 'w', encoding='utf-8') as f:
    #     f.write(to_blackletter(string.ascii_letters))

    if len(sys.argv) < 2:
        print("You must choose a mode, tweet or local")
        sys.exit(1)

    if sys.argv[1] not in ['local', 'tweet']:
        print("Incorrect mode")
        sys.exit(2)

    if sys.argv[1] == 'local':
        print('local mode')
        output = print
        branch_getter = lambda: choice([i for i in range(8)])

    elif sys.argv[1] == 'tweet':
        print('tweet mode')
        output = tweet
        branch_getter = get_branch_number

    sentences = [create_sentence() for _ in range(8)]


    branch_number = branch_getter()
    # print('Creating branch...')
    # print(f'You are on branch {branch_number+1}')
    # print(sentences[branch_number])

    NUMBERS = [
        "\N{ROMAN NUMERAL ONE}",
        "\N{ROMAN NUMERAL TWO}",
        "\N{ROMAN NUMERAL THREE}",
        "\N{ROMAN NUMERAL FOUR}",
        "\N{ROMAN NUMERAL FIVE}",
        "\N{ROMAN NUMERAL SIX}",
        "\N{ROMAN NUMERAL SEVEN}",
        "\N{ROMAN NUMERAL EIGHT}"
    ]

    message = (
        to_blackletter("Splintering the multiverse...\n")
        + to_blackletter("You are now on branch ")
        + NUMBERS[branch_number]
    )


    output( message )

    sentence = sentences[branch_number]

    output(sentence.blackletter)
    print(sentence.normal)
