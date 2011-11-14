"""
This is a code for managing my time in a simple and orderly fashion.
Richard Littauer

Goal: a worksheet with week, day, start, end, total, task, comment. 

python mask.py begin <project>
python mask.py status
python mask.py end <project> <comment>
"""

import time
import datetime
import sys

output_file_name = "oxygen_log.csv"

if (sys.argv[1] == "begin"):
    f = open(output_file_name,'a')
    print "Mask on!"
    f.write(str(datetime.datetime.now()) + ", ")
    project = sys.argv[2]
    f.write(project + ",")
    f.close()

if (sys.argv[1] == "end"):
    f = open(output_file_name, 'r+')
    lineList = f.readlines()
    on = lineList[-1]
    off = str(datetime.datetime.now())
    from datetime import datetime
    FMT = '%H:%M:%S'
    tdelta = datetime.strptime(off[11:19], FMT) - datetime.strptime(on[11:19], FMT)
    print 'Mask off! You were on the surface of Pandora from ' + on.replace(", ", "") + ' to ' + off + ' and survived for ' + str(tdelta) + '.'
    comment = sys.argv[3]
    project = sys.argv[2]
    print 'Operation ' + project + ' is now terminated. Your activity report readout: ' + comment
    f.write(str(off) + ", ")
    f.write(str(tdelta) + ", ")
    f.write(project + ", ")
    f.write(comment)
    f.write("\n")
    f.close()

if (sys.argv[1] =="status"):
    f = open(output_file_name, 'r')
    lineList = f.readlines()
    if len(lineList[-1]) <= 40:
        on = lineList[-1].replace(", ", ". Your current Operation: ").replace(",", ".")
        print "You are currently on the job in Pandora. Your last signal was at " + on
    else:
        print "Night lies over Isengard."
