#!/Library/Frameworks/Python.framework/Versions/Current/bin/python
#-*- coding: utf-8 -*-

import sys
from datetime import datetime

folder_path = '/Users/richardlittauer/Code/'
output_file_name = folder_path + '/hogwarts, a history.md'

def write(input):
    f = open(output_file_name,'r+')
    f.readlines()

    time_now = datetime.now()

    f.write(str(time_now) + '\t' + input + '\n')
    f.close()

    print 'Written.'

if __name__ == "__main__":
    try:
        input = sys.argv[2]
        write(input)
    except IndexError:
        input = raw_input('Rmemeber what?\t')
        write(input)

