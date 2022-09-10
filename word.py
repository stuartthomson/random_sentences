from typing import List, NamedTuple
import string

# string.punctuation doesn't have everything
_PUNCT_LIST = string.punctuation + '”“’‘'

BLACKLETTER_CODE = {
    65: u'\U0001d504',
    66: u'\U0001d505',
    67: u'\U0001d56e',
    68: u'\U0001d507',
    69: u'\U0001d508',
    70: u'\U0001d509',
    71: u'\U0001d50a',
    72: u'\U0001d573',
    73: u'\U0001d574',
    74: u'\U0001d50d',
    75: u'\U0001d50e',
    76: u'\U0001d50f',
    77: u'\U0001d510',
    78: u'\U0001d511',
    79: u'\U0001d512',
    80: u'\U0001d513',
    81: u'\U0001d514',
    82: u'\U0001d57d',
    83: u'\U0001d516',
    84: u'\U0001d517',
    85: u'\U0001d518',
    86: u'\U0001d519',
    87: u'\U0001d51a',
    88: u'\U0001d51b',
    89: u'\U0001d51c',
    90: u'\U0001d585',
    97: u'\U0001d51e',
    98: u'\U0001d51f',
    99: u'\U0001d520',
    100: u'\U0001d521',
    101: u'\U0001d522',
    102: u'\U0001d523',
    103: u'\U0001d524',
    104: u'\U0001d525',
    105: u'\U0001d526',
    106: u'\U0001d527',
    107: u'\U0001d528',
    108: u'\U0001d529',
    109: u'\U0001d52a',
    110: u'\U0001d52b',
    111: u'\U0001d52c',
    112: u'\U0001d52d',
    113: u'\U0001d52e',
    114: u'\U0001d52f',
    115: u'\U0001d530',
    116: u'\U0001d531',
    117: u'\U0001d532',
    118: u'\U0001d533',
    119: u'\U0001d534',
    120: u'\U0001d535',
    121: u'\U0001d536',
    122: u'\U0001d537'
}

class Word(NamedTuple):
    """
    Represents a word
    """
    text: str
    pos: str

    def is_proper_noun(self) -> bool:
        return self.pos == 'NNP'

    def capitalize(self) -> 'Word':
        return Word(
            text=self.text.capitalize(),
            pos=self.pos
        )

    def lower(self) -> 'Word':
        return Word(
            text = self.text.lower(),
            pos = self.pos
        )

    def is_punct(self) -> bool:
        return self.text in _PUNCT_LIST

    def is_ascii(self) -> bool:
        try:
            self.text.encode('ascii')
            return True
        except UnicodeEncodeError:
            print(f"Not ASCII: {self}")
            return False

    def is_allowed_in_dict(self) -> bool:
        return self.is_ascii() and not self.is_punct()


Sentence = List[Word]
