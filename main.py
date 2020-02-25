import nltk
# nltk.download('tagsets')
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
from nltk import word_tokenize
from tqdm import tqdm
from collections import defaultdict
from random import choice

import grammar_check
tool = grammar_check.LanguageTool('en-GB')


words_dict = defaultdict(list)
sentence_structure_list = []

with open('./data/Genesis.txt', 'r') as fl:

    for i, line in tqdm(enumerate(fl)):

        sentence = []
        for word, pos in nltk.pos_tag(word_tokenize(line)):
            words_dict[pos].append(word)
            sentence.append(pos)

        sentence_structure_list.append(sentence)

for i in range(20):
    structure = choice(sentence_structure_list)
    words = [choice(words_dict[pos]) for pos in structure]
    sentence = ' '.join(words)
    print(sentence)