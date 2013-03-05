#!/Library/Frameworks/Python.framework/Versions/Current/bin/python
#-*- coding: utf-8 -*-

"""
This is just a script that makes a response every time I yell at my computer.
Make an alias and change the responses, if you like.

All the licenses are on this beast. 
"""

import random

library = [
  'Oswald was a fag.',
  'Do it for the boat people.',
  'brain dog is dead'
        ]

if __name__ == '__main__':
	print library[random.randrange(0,len(library))]
