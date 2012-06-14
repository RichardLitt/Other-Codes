'''
Dissertation rewrite, as an older coder.
'''

from sys import argv
import random

output = '-'.join(argv[1:])+ '.csv'

#function-WPT-word.length-possible.syllables-lexicon.size-amount.of.words.in.corpus-initial.lex-random.initial.lex-generations.

n = int(argv[3]) # Length of the n-grams (henceforth, words)
s = int(argv[4]) # Size of the alphabet
l = int(argv[5]) # Size of the lexicon
b = int(argv[6]) # Amount of words to use - this creates a bottleneck
## This is seemingly hardcoded and ignored in the original.
## Probably a major bug, actually. 
i = int(argv[7]) # The iterations

'''
The following create regular lexicons as controls.
'''

## In each of these, s is not taken into account, although it should be.

regular_word = ''.join([ str(x) for x in range(n) ])

# Entirely regular, same locations ('01234')
lexicon1 = [ regular_word for x in range(l) ]

# Entirely regular, equal weighting for all locations ('40123' &c.)
def create_lexicon_2(n,l):
    lexicon2 = []
    regular_word = [ str(x) for x in range(n) ]
    for x in range(l):
        lexicon2.append(''.join(regular_word))
        regular_word += regular_word.pop(0)
    return lexicon2

lexicon2 = create_lexicon_2(n,l)

# Entirely regular, every other reversed ('01234', '43210')
def create_lexicon_3(n,l):
    lexicon3 = []
    regular_word = [ str(x) for x in range(n) ]
    for x in range(l):
        lexicon3.append(''.join(regular_word))
        regular_word.reverse()
    return lexicon3

lexicon3 = create_lexicon_3(n,l)

'''
These create the random lexicons
'''

## Why am I using only ints? Would be good to use alphabetical characters,too,
## as they have a wider range.

# Creates a word
def word(n,s):
    return [ str(random.randint(0,s)) for x in range(l) ]

##; ; ; STOPPED HERE

# This lexicon has no internal words, and is merely random
def random_lexicon(s,n,l): 
    p = []
    p.append(''.join(word(s,;l))
    return p[0]

print random_lexicon(s,n,l)

