"""
This is a code for managing my time in a simple and orderly fashion.
Richard Littauer

Goal: a worksheet with week, day, start, end, total, task, comment. 

python timestamp.py <begin/end> <project> <comment>
"""

import time
import datetime
import sys

output_file_name = "oxygen_log.csv"

if (sys.argv[1] == "start"):
    output = open(output_file_name,'a')
    print "Mask on!"
    output.write(str(datetime.datetime.now()) + ", ",)
    output.close()

if (sys.argv[1] == "stop"):
    f = open(output_file_name,'r+')
    #print f.read()
    #print f.readline()

    f = open(output_file_name, 'r+')
    lineList = f.readlines()
    #print (lineList)
    #print ("The last line is:")
    #print (lineList[len(lineList)-1])
    # or simply
    on = lineList[-1]
    off = str(datetime.datetime.now())
    from datetime import datetime
    FMT = '%H:%M:%S'
    tdelta = datetime.strptime(off[11:19], FMT) - datetime.strptime(on[11:19], FMT)
    print 'Mask off! You wore your mask on Pandora from ' + on.replace(", ", "") + ' to ' + off + ' and survived for a total of ' + str(tdelta) + '.'
    #print (lineList[-1])
    comment = sys.argv[3]
    project = sys.argv[2]
    #f.write("\"" + str(off) + "\", \"" + str(tdelta) + "\", \"" + project + "\", \"" + comment + "\"")
    f.write(str(off) + ", ")
    f.write(str(tdelta) + ", ")
    f.write(project + ", ")
    f.write(comment)
    f.write("\n")
    f.close()



