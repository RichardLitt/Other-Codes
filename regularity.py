'''
Regularity in word length testing
Richard Littauer

Issues: Need to take into account that aba is different from bab, while not
ignoring 

'''

import random
import os
import sys

lexicon_size = int(20)
word_length = 5
phonemes = 9

lexicon = ['010', '0122', '013988910', '1921', '151']
print lexicon

def palindrome():
    for x in lexicon:
        for y in range(len(x)/2+1):
            if x[y] == x[-y-1]:
                print x[y], x[-y-1], y

def syllables():
    for x in lexicon:
        for y in range(len(x),len(x)):
            print y



'''
def lexicon():
    lexicon = []
    for z in range(lexicon_size):
        for x in random.randrange(word_length):
            word = []
            for y in random.randrange(0,phonemes):
                word.append(y)
            ''.join(word)
            print word
        lexicon.append(word)
    print lexicon
'''

if __name__ == "__main__":
    if (sys.argv[1] == "run"):
        palindrome()
