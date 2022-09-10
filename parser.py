from typing import Dict, List
from collections import defaultdict

from nltk.data import load
from word import Sentence, Word

import nltk
nltk.download('tagsets')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
from nltk import word_tokenize
from blackletter import encodeCode

import pickle

class Parser:
    _filenames: List[str]
    _words_dict: Dict[str, List[str]] = defaultdict(list)

    # Do I actually want to store this?
    # Yes, some words we don't scramble or something?
    # TODO: Check what we need
    _sentences: List[Sentence] = []

    def __init__(self, filenames: List[str]) -> None:
        self._filenames = filenames
        for filename in self._filenames:
            print(filename)
            self._parse_file(filename)

    def _parse_file(self, filename: str) -> None:
        """
        Parse a file and add the contents to this Parser instance
        """
        with open(filename, 'r', encoding='utf-8') as infile:
            for line in infile:
                sentence = [Word(text=text, pos=pos) for text, pos  in nltk.pos_tag(word_tokenize(line))]
                self._sentences.append(sentence)

                for word in sentence:
                    if word.is_allowed_in_dict():
                        self._words_dict[word.pos].append(word.text)

    @property
    def filenames(self) -> List[str]:
        return self._filenames

    @property
    def sentences(self) -> List[Sentence]:
        return self._sentences

    @property
    def words_dict(self) -> Dict[str, List[str]]:
        return self._words_dict

    def dump_sentences(self, filename: str) -> None:
        """
        Pickles the sentences
        """
        pickle.dump(self._sentences, open(filename, 'wb'))

    def dump_words_dict(self, filename: str) -> None:
        """
        Pickles the words dictionary
        """
        pickle.dump(self._words_dict, open(filename, 'wb'))

if __name__ == '__main__':
    from glob import glob
    parser = Parser(glob('./data/fixed/*'))
    # parser.dump_sentences('./sentences.pickle')
    # parser.dump_words_dict('./ascii_words.pickle')

    # TODO: blackletter will confuse language tool, need to do this after-the-fact

    # loaded_sents = pickle.load(open('./sentences.p', 'rb'))

    # print(loaded_sents[:10])
