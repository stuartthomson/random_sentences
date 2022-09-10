from blackletter import to_bold_blackletter
from typing import Dict, List
from word import Word
import random

_PROPER_NOUNS = [
    to_bold_blackletter('Octopus'),
    to_bold_blackletter('Lion'),
    to_bold_blackletter('Brigdi'),
    to_bold_blackletter('Monad'),
    to_bold_blackletter('Dyad'),
    to_bold_blackletter('Entropy'),
    to_bold_blackletter('Number')
]

class SentenceScrambler:
    def __init__(self, sentence: List[Word], word_dict: Dict[str, List[str]]) -> None:
        self._sentence = sentence
        self.word_dict = word_dict

    def _create_piece(self, word: Word, should_capitalise: bool, add_space: bool) -> str:

        sp = ' ' if add_space else ''

        if word.is_punct():
            if word.text in '"”“':
                return sp + word.text
            return word.text

        if word.is_proper_noun():
            return sp + word.text

        if word.text.lower() == 'i':
            return sp + 'I'

        if should_capitalise:
            return sp + word.text.capitalize()

        return sp + word.text.lower()

    def scramble(self) -> str:
        sentence = ''
        should_capitalise = True

        for new_word in [self.replace_word(word) for word in self._sentence]:
            sentence += self._create_piece(new_word, should_capitalise, True)
            should_capitalise = new_word.text in ['!', '.']

        return sentence.lstrip(' ')

    def replace_word(self, word: Word) -> Word:
        """
        Choose a replacement word for a given word
        """
        if word.is_punct():
            return word

        if word.is_proper_noun():
            return Word(
                text=random.choice(_PROPER_NOUNS),
                pos=word.pos
            )

        potential_word = Word(
            text=random.choice(self.word_dict[word.pos]),
            pos=word.pos
        )

        if potential_word.text == 'ye' or potential_word.text == 'Ye':
            potential_word = Word(
                text='you',
                pos=word.pos
            )

        return potential_word
