"""
This is a code for managing my time in a simple and orderly fashion.
Richard Littauer

Goal: a worksheet with week, day, start, end, total, task, comment. 

python mask.py begin <project>
python mask.py status
python mask.py end <project> <comment>
"""
#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import time
import datetime
import sys
import re
import dis
import random
import math
import textwrap

output_file_name = "oxygen_log.csv"


pay_so_far = "556 euro"

work_tasks = ["hiwi", "FLST", "PSR", "syntax", "CL4LRL"]


def help():
    print
    print "-------------------Help Desk-------------------"
    print
    print " begin <project> [last]/[%d | backtime]"
    print " end <project> <\"comment\">/<\"-x\">/<\"-c\"> [%d | backtime]" 
    print " fence <project> <on> <off> <comment>/<\"-x\">/<\"-c\"> "
    print " status"
    print " cease"
    print " topics"
    print
    print " search <project> [print]"
    print " today [-][project]/[left]"
    print " yesterday"
    print " week <%d> [days to search]"
    print " hiwi [print]/[%d | total to work] "
    print " test"
    print
    print "-----------------------------------------------"
    print




def print_time_labels(input_time):
    if len(input_time) == 16:
        input_time = input_time[-8:]
    if len(input_time) == 7:
        hours = int(input_time[:1])
        minutes = int(input_time[2:4])
        seconds = int(input_time[5:7])
    if len(input_time) == 8:
        hours = int(input_time[:2])
        minutes = int(input_time[3:5])
        seconds = int(input_time[6:8])
    hour_string = "hours"
    minute_string = "minutes"
    second_string = "seconds"
    if hours == 1:
        hour_string = "hour"
    if minutes == 1:
        minute_string = "minute"
    if seconds == 1:
        second_string = "second"
    output = "%s %s, %s %s, and %s %s" % (hours, hour_string, minutes, minute_string, seconds, second_string)
    if hours == 0:
        output = "%s %s and %s %s" % (minutes, minute_string, seconds, second_string)
    if minutes == 0:
        output = "%s %s and %s %s" % (hours, hour_string, seconds, second_string)
    if seconds == 0:
        output = "%s %s and %s %s" % (hours, hour_string, minutes, minute_string)
    if (seconds == 0) and (hours == 0):
        output = "%s %s" % (minutes, minute_string)
    return output

def random_navi_animal():
    animal = ["'angts\xcck", "eltungawng", "ngawng", "fpxafaw", "ikran",
            "ikranay", "kali'weya", "lenay'ga", "lonataya", "nantang",
            "pa'li", "palulukan", "riti", "talioang", "teylu", "toruk",
            "yerik", "yomh\xcc'ang", "hi'ang", "zize'"]
    return str(animal[random.randrange(len(animal)-1)])

def test():
   print "Looks like you're not testing anything at the moment."

def begin():
    f = open(output_file_name,'a')
    print
    print "Mask on!"
    time_now = datetime.datetime.now()
    try:
        pattern = re.compile("\d+")
        match_o = re.match(pattern, sys.argv[3])
        if (match_o != None):
            today = datetime.datetime.now()
            min_change = datetime.timedelta(minutes=int(sys.argv[3]))
            time_adjust = today - min_change
            print "-----------------------------------------------------------------------"
            print "You have just adjusted time backwards: " 
            print str(time_now) + " is now " + str(time_adjust) + "."
            print "-----------------------------------------------------------------------"
            time_now = time_adjust
    except: x = "There should be another option here."
    try:
        if sys.argv[3] == "-l":
            f = open(output_file_name, 'r+')
            lineList = f.readlines()
            on = lineList[-1]
            pattern = re.compile("\d\d:\d\d:\d\d.\d+")
            match_o_time = re.search(pattern, on[27:])
            if (match_o_time != None):
                time_now = str(time_now)[:10] + " " + match_o_time.group(0)
                print "-----------------------------------------------------------------------"
                print "You have just adjusted your start level from the last known signal, at " + time_now + "."
                print "-----------------------------------------------------------------------"
    except: x = "This is a filler. You are in real time."
    print
    f.write(str(time_now) + ", ")
    project = sys.argv[2]
    f.write(project + ", ")
    f.close()


def end():
    f = open(output_file_name, 'r+')
    from datetime import datetime
    from datetime import timedelta
    lineList = f.readlines()
    on = lineList[-1]
    off = datetime.now()
    print
    print "---------------------------------End------------------------------------"
    print 'Mask off!'
    try:
        pattern = re.compile("\d+")
        match_o = re.match(pattern, sys.argv[4])
        if (match_o != None):
            today = datetime.now()
            min_change = timedelta(minutes=int(sys.argv[4]))
            time_adjust = today - min_change
            print "You have just adjusted time backwards: " + str(off) + " is now " + str(time_adjust) + "."
            off = time_adjust
    except: x = "penguins"
    off = str(off)
    FMT = '%H:%M:%S'
    tdelta = datetime.strptime(off[11:19], FMT) - datetime.strptime(on[11:19], FMT)
    total_time = str(tdelta)
    if len(total_time) == 15:
        total_time = total_time[-7:]
    if len(total_time) == 16:
        total_time = total_time[-8:]
    print 'You were on the surface of Pandora from: ' + on[:19] + ' to ' + off[11:19] + '.'
    time_labels = print_time_labels(total_time)
    comment = sys.argv[3].replace(', ', ',')
    if comment == "-x":
        comment = ""
    if comment == "-c":
        comment = "Class."
    project = sys.argv[2]
    try:
        pattern = re.compile("\d+")
        match_o = re.match(pattern, comment)
        if (match_o != None):
                print "You survived for %s, and killed like %s nantangs." % (time_labels, match_o.group())
        if (match_o == None):
                print "You survived for %s." % time_labels
    except: x = "moose"
    print 'Operation ' + project + ' is now terminated. Your activity report readout: '
    print comment
    print "------------------------------------------------------------------------"
    f.write(str(off) + ", ")
    f.write(total_time + ", ")
    f.write(project + ", ")
    f.write(comment.replace("\"", "'"))
    f.write("\n")
    f.close()


def status():
    f = open(output_file_name, 'r')
    from datetime import datetime
    lineList = f.readlines()
    print 
    print "---------------------------------Status---------------------------------"
    if lineList[-1][-2] != ",":
        f = open(output_file_name, 'r+')
        lineList = f.readlines()
        on = lineList[-1]
        #Clean this us using split()
        try:
            pattern_time = re.compile("\d\d:\d\d\:\d\d.\d+")
            match_o_time = re.search(pattern_time, on[29:])
            if (match_o_time != None):
                onn = match_o_time.group(0)
                off = str(datetime.now())
                FMT = '%H:%M:%S'
                time_since = datetime.strptime(off[11:19], FMT) - datetime.strptime(onn[:8], FMT)
                time_since = str(time_since)
        except: x = "I am a whale"
        time_labels = print_time_labels(time_since)
        print "You have not been working for %s." % time_labels
        print
        on = on.replace('\n', '').split(', ')
        print "Your last job, %s, lasted %s. Comment: \n%s" % (on[4], print_time_labels(on[3]), on[5])
        if len(time_since) >= 10:
            print "Good morning. You haven't started working yet today."
            print "Your last read out was: " + on.replace("\n","")
    if len(lineList[-1]) <= 40:
        on = lineList[-1]
        last_job = on[28:].replace(",", "").replace(" ", "")
        off = str(datetime.now())
        FMT = '%H:%M:%S'
        tdelta = datetime.strptime(off[11:19], FMT) - datetime.strptime(on[11:19], FMT)
        on = lineList[-1].replace(", ", ". Your current Operation: ").replace(",", ".")
        print 'You are currently on project \'' + last_job + '\' in Pandora.'
        print 'Your last signal was at ' + on[:19] + '. Time alive: ' + str(tdelta) + '.'
    print "------------------------------------------------------------------------"
    print ""
    f.close()


def cease():
    f = open(output_file_name, 'r+')
    lineList = f.readlines()
    on = lineList[-1]
    from datetime import datetime
    from datetime import timedelta
    off = datetime.now()
    off = str(off)
    from datetime import datetime
    FMT = '%H:%M:%S'
    tdelta = datetime.strptime(off[11:19], FMT) - datetime.strptime(on[11:19], FMT)
    print
    print "---------------------------------Cease----------------------------------"
    print 'Mask off!'
    print 'You were on the surface of Pandora from ' + on[:19] + ' to ' + off[:19]
    print 'You survived for ' + str(tdelta) + '.'
    print 'What ho?! A break?'
    print "------------------------------------------------------------------------"
    print
    f.write(str(off) + ", ")
    f.write(str(tdelta) + ", ")
    project = on.split(', ')[1]
    f.write(project + ", ")
    f.write("")
    f.write("\n")
    f.close()


def search():
    f = open(output_file_name, 'r+')
    lineList = f.readlines()
    from datetime import datetime
    from datetime import timedelta
    total_time = "00:00:00"
    print
    print "---------------------------------Search---------------------------------"
    for line in lineList:
        pattern = re.compile(sys.argv[2])
        match_o = re.search(pattern, line)
        if (match_o != None):
            pattern_time = re.compile("\d+\:\d\d\:\d\d\,")
            match_o_time = re.search(pattern_time, line)
            if (match_o_time != None):
                match_o_t = str(match_o_time.group(0)).replace(",", "")
                FMT = '%H:%M:%S'
                tt = datetime.strptime(match_o_t, FMT)
                total_time = datetime.strptime(str(total_time), FMT) + timedelta(hours=tt.hour,minutes=tt.minute,seconds=tt.second)
                total_time = str(total_time)[11:]
            try:
                if (sys.argv[3] == "print"):
                    line = line.split(', ')
                    line[5] = line[5].replace("\n", "")
                    print line[0][5:11] + "for " + print_time_labels(line[3]) + ": " + line[5]
            except: x = "This is a filler."
    if sys.argv[2] == "coding":
        print "You have worked on this project for %s." % print_time_labels(total_time)
    if sys.argv[2] != "coding":
        print "You have worked on %s for %s." % (sys.argv[2], print_time_labels(total_time))
    print "------------------------------------------------------------------------"
    print
    f.close()

def today():
    from datetime import datetime
    from datetime import timedelta
    f = open(output_file_name, 'r')
    lineList = f.readlines()
    time_now = datetime.now()
    print 
    print "---------------------------------Today---------------------------------"
    total_time = "00:00:00"
    total_time_alt = "00:00:00"
    logged_time = "00:00:00"
    specific_job_catch = "empty"
    for line in lineList:
        line = line.replace('\n', '').split(', ')
        if str(time_now)[:10] == line[0][:10]:
            if len(line) == 3:
                #if line[1] in work_tasks:
                on = line[0]
                off = str(datetime.now())
                FMT = '%H:%M:%S'
                tdelta = datetime.strptime(off[11:19], FMT) - datetime.strptime(on[11:19], FMT)
                on = lineList[-1].replace(", ", ". Your current Operation: ").replace(",", ".")
                worked = str(tdelta)
                read_out = "Ongoing..."
            if len(line) > 3:
                #if line[1] in work_tasks:
                worked = line[3]
                read_out = line[5]
            time_labels = print_time_labels(worked)
            read_out_block = "%s for %s: %s" % (line[1], time_labels, read_out)
            dedented_text = textwrap.dedent(read_out_block).strip()
            print textwrap.fill(dedented_text, initial_indent='', subsequent_indent='    ')
            FMT = '%H:%M:%S'
            lt = datetime.strptime(worked, FMT)
            logged_time = datetime.strptime(str(logged_time), FMT) + timedelta(hours=lt.hour,minutes=lt.minute,seconds=lt.second)
            logged_time = str(logged_time)[11:]
            if line[1] in work_tasks:
                    tt = datetime.strptime(worked, FMT)
                    total_time = datetime.strptime(str(total_time), FMT) + timedelta(hours=tt.hour,minutes=tt.minute,seconds=tt.second)
                    total_time = str(total_time)[11:]
            try:
                if sys.argv[2][0] == "-":
                    if (line[1] != sys.argv[2]):
                        FMT = '%H:%M:%S'
                        tdelta = datetime.strptime(total_time, FMT) - datetime.strptime(line[3], FMT)
                        total_time_alt = str(tdelta)
                    specific_job = sys.argv[2][1:]
                    specific_job_catch = "except"
            except: penguins = "penguins"
            try:
                if sys.argv[2][0] != "-":
                    if (line[1] == sys.argv[2]):
                        tt = datetime.strptime(worked, FMT)
                        total_time_alt = datetime.strptime(str(total_time_alt), FMT) + timedelta(hours=tt.hour,minutes=tt.minute,seconds=tt.second)
                        total_time_alt = str(total_time_alt)[11:]
                        specific_job = line[1]
                        specific_job_catch = "only"
            except: specific_job = "essential work"
    productivity_measure = (float(total_time[:2])*60+float(total_time[3:5]))/504*100
    print
    print "You have worked a total of %s today." % print_time_labels(total_time)
    if total_time != logged_time:
        print "(But you've logged %s.)" % print_time_labels(logged_time)
    print "So far, you have been %.2f%% productive." % productivity_measure
    try: 
        if (sys.argv[2] == "left"):
            time_left = 504-(float(total_time[:2])*60+float(total_time[3:5]))
            time_left_fmt = str(int((time_left-time_left%60)/60)) + ":" + str(int(time_left%60)) + ":00"
            print "You only have %s left to go!" % print_time_labels(time_left_fmt)
    except: daw = "d'awwwww"
    if specific_job_catch == "except":
        time_labels = print_time_labels(total_time_alt)
        print "Of that, you did everything but %s for %s." % (specific_job, time_labels)
    if specific_job_catch == "only":
        time_labels = print_time_labels(total_time_alt)
        print "Of that, you did %s for %s." % (specific_job, time_labels)
    print "-----------------------------------------------------------------------"
    print 

def yesterday():
    from datetime import datetime
    from datetime import timedelta
    f = open(output_file_name, 'r')
    lineList = f.readlines()
    time_now = datetime.now()
    print 
    print "-----------------------------Yesterday---------------------------------"
    total_time = "00:00:00"
    total_time_alt = "00:00:00"
    logged_time = "00:00:00"
    specific_job_catch = "empty"
    for line in lineList:
        line = line.replace('\n', '')
        today_date = str(time_now)[:10]
        if int(today_date[8:]) < 30:
            modify_date = int(today_date[8:])-1
            today_date = today_date[:8] + str(modify_date)
        if int(today_date[8:]) >= 30: print "Uh. End of month. Awkward."
        line  = line.split(', ')
        if today_date == line[0][:10]:
            worked = line[3]
            read_out = line[5]
            time_labels = print_time_labels(worked)
            read_out_block = "%s for %s: %s" % (line[1], time_labels, read_out)
            dedented_text = textwrap.dedent(read_out_block).strip()
            print textwrap.fill(dedented_text, initial_indent='', subsequent_indent='    ')
            FMT = '%H:%M:%S'
            lt = datetime.strptime(worked, FMT)
            logged_time = datetime.strptime(str(logged_time), FMT) + timedelta(hours=lt.hour,minutes=lt.minute,seconds=lt.second)
            logged_time = str(logged_time)[11:]
            if line[1] in work_tasks:
                tt = datetime.strptime(worked, FMT)
                total_time = datetime.strptime(str(total_time), FMT) + timedelta(hours=tt.hour,minutes=tt.minute,seconds=tt.second)
                total_time = str(total_time)[11:]
    productivity_measure = (float(total_time[:2])*60+float(total_time[3:5]))/504*100
    print
    print "You worked a total of %s yesterday." % print_time_labels(total_time)
    print "(But you logged %s.)" % print_time_labels(logged_time)
    print "You were %.2f%% productive." % productivity_measure
    print "-----------------------------------------------------------------------"
    print 

def this_week():
    from datetime import datetime
    from datetime import timedelta
    f = open(output_file_name, 'r')
    lineList = f.readlines()
    time_now = datetime.now()
    print 
    print "-----------------------------This Week---------------------------------"
    work_totality = "00:00:00"
    productivity = 0
    for x in range(int(sys.argv[2])):
        total_time = "00:00:00"
        total_time_alt = "00:00:00"
        logged_time = "00:00:00"
        specific_job_catch = "empty"
        for line in lineList:
            line = line.replace('\n', '')
            today_date = str(time_now)[:10]
            if int(today_date[8:]) < 30:
                modify_date = int(today_date[8:])-x
                today_date = today_date[:8] + str(modify_date)
            if int(today_date[8:]) >= 30: print "Uh. End of month. Awkward."
            line  = line.split(', ')
            if today_date == line[0][:10]:
                if len(line) == 3:
                    #if line[1] in work_tasks:
                    on = line[0]
                    off = str(datetime.now())
                    FMT = '%H:%M:%S'
                    tdelta = datetime.strptime(off[11:19], FMT) - datetime.strptime(on[11:19], FMT)
                    on = lineList[-1].replace(", ", ". Your current Operation: ").replace(",", ".")
                    worked = str(tdelta)
                    read_out = "Ongoing..."
                    FMT = '%H:%M:%S'
                    lt = datetime.strptime(worked, FMT)
                    logged_time = datetime.strptime(str(logged_time), FMT) + timedelta(hours=lt.hour,minutes=lt.minute,seconds=lt.second)
                    logged_time = str(logged_time)[11:]
                    if line[1] in work_tasks:
                        tt = datetime.strptime(worked, FMT)
                        total_time = datetime.strptime(str(total_time), FMT) + timedelta(hours=tt.hour,minutes=tt.minute,seconds=tt.second)
                        total_time = str(total_time)[11:]
                        work_totality = datetime.strptime(str(work_totality), FMT) + timedelta(hours=tt.hour,minutes=tt.minute,seconds=tt.second)
                        work_totality = str(work_totality)[11:]
                if len(line) > 3:
                    worked = line[3]
                    read_out = line[5]
                    time_labels = print_time_labels(worked)
                    #read_out_block = "%s for %s: %s" % (line[1], time_labels, read_out)
                    #dedented_text = textwrap.dedent(read_out_block).strip()
                    #print textwrap.fill(dedented_text, initial_indent='', subsequent_indent='    ')
                    FMT = '%H:%M:%S'
                    lt = datetime.strptime(worked, FMT)
                    logged_time = datetime.strptime(str(logged_time), FMT) + timedelta(hours=lt.hour,minutes=lt.minute,seconds=lt.second)
                    logged_time = str(logged_time)[11:]
                    if line[1] in work_tasks:
                        tt = datetime.strptime(worked, FMT)
                        total_time = datetime.strptime(str(total_time), FMT) + timedelta(hours=tt.hour,minutes=tt.minute,seconds=tt.second)
                        total_time = str(total_time)[11:]
                        work_totality = datetime.strptime(str(work_totality), FMT) + timedelta(hours=tt.hour,minutes=tt.minute,seconds=tt.second)
                        work_totality = str(work_totality)[11:]
        productivity_measure = (float(total_time[:2])*60+float(total_time[3:5]))/504*100
        productivity += productivity_measure
        print
        if x == 0: print "You've worked %s today." % \
            print_time_labels(total_time)
        if x == 1:
            print "You worked a total of %s yesterday." % \
            print_time_labels(total_time)
        if x >= 2:
            print "You worked a total of %s %s days ago." % \
        (print_time_labels(total_time), x)
        try:
            if sys.argv[3] == "logged":
                print "(But you logged %s.)" % print_time_labels(logged_time)
        except: penguins = "penguins"
        print "You were %.2f%% productive." % productivity_measure
    productivity = productivity / float(int(sys.argv[2]))
    print 
    print "This week, you have worked %s." % print_time_labels(work_totality)
    if productivity < 20:
        print "You are and were really lazy and inept." 
    if productivity < 50:
        print "You were only %s%% productive" % productivity
    if productivity >= 50:
        print "You were %s%% productive." % productivity
    if productivity >= 100:
        print "Well done. You were really fucking productive. %s%%, to be \
        exact." % productivity
    print "-----------------------------------------------------------------------"
    print 


def topics():
    import pprint
    f = open(output_file_name, 'r+')
    lineList = f.readlines()
    topics = []
    print
    print "---------------------------------Topics---------------------------------"
    for line in lineList:
        line = line.split(', ')
        topics.append(line[1])
    set = {} 
    map(set.__setitem__, topics, []) 
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(set.keys())
    print "------------------------------------------------------------------------"

def fence():
    f = open(output_file_name,'r+')
    from datetime import datetime
    from datetime import timedelta
    time_now = datetime.now()
    lineList = f.readlines()
    last_line = lineList[-1].split(', ')
    ## Make sure that there isn't any current job
    if len(last_line) != 6:
        print
        print "      *****************************"
        print "      *Last job unfinished, error.*"
        print "      *****************************"
        print
    if len(last_line) == 6:
        print 
        print "-------------------------------Fence------------------------------------"

    ## Find the first time. 
    pattern = re.compile("\d+:\d+")
    match_o = re.match(pattern, sys.argv[3])
    if (match_o != None):
        today = str(datetime.now())
        pattern = re.compile("\d+:")
        match_h = re.match(pattern, sys.argv[3])
        if (match_h != None):
            today = today[:11] + match_h.group(0) + today[14:]
            on = today[:14] + sys.argv[3][-2:] + ":00.000000"

    ## Find the second time. 
    pattern = re.compile("\d+:\d+")
    match_o = re.match(pattern, sys.argv[4])
    if (match_o != None):
        today = str(datetime.now())
        pattern = re.compile("\d+:")
        match_h = re.match(pattern, sys.argv[4])
        if (match_h != None):
            today = today[:11] + match_h.group(0) + today[14:]
            off = today[:14] + sys.argv[4][-2:] + ":00.000000"

    ## Compute the total time. 
    off = str(off)
    FMT = '%H:%M:%S'
    tdelta = datetime.strptime(off[11:19], FMT) - datetime.strptime(on[11:19], FMT)
    total_time = str(tdelta)
    if len(total_time) == 15:
        total_time = total_time[-7:]
    if len(total_time) == 16:
        total_time = total_time[-8:]
    print 'You were on the surface of Pandora from: ' + on[:19] + ' to ' + off[11:19] + '.'
    time_labels = print_time_labels(total_time)
    comment = sys.argv[5].replace(', ', ',')
    if comment == "-x":
        comment = ""
    if comment == "-c":
        comment = "Class."
    project = sys.argv[2]
    try:
        pattern = re.compile("\d+")
        match_o = re.match(pattern, comment)
        if (match_o != None):
                print "You survived for %s, and killed like %s nantangs." % (time_labels, match_o.group())
        if (match_o == None):
                print "You survived for %s." % time_labels
    except: x = "moose"
    
    print 'Operation ' + project + ' is now terminated. Your activity report readout: '
    print comment
    print "------------------------------------------------------------------------"
    print 
    
    ## Write to output file.
    f.write(str(on) + ", ")
    f.write(project + ", ")
    f.write(str(off) + ", ")
    f.write(total_time + ", ")
    f.write(project + ", ")
    f.write(comment.replace("\"", "'"))
    f.write("\n")
    f.close()


if __name__ == "__main__":
    if (sys.argv[1] == "test"):
        test()
    if (sys.argv[1] == "today"):
        today()
    if (sys.argv[1] == "hiwi"):
        hiwi()
    if (sys.argv[1] == "search"):
        search()
    if (sys.argv[1] == "cease"):
        cease()
    if (sys.argv[1] == "status"):
        status()
    if (sys.argv[1] == "end"):
        end()
    if (sys.argv[1] == "begin"):
        begin()
    if (sys.argv[1] == "help"):
        help()
    if (sys.argv[1] == "yesterday"):
        yesterday()
    if (sys.argv[1] == "topics"):
        topics()
    if (sys.argv[1] == "week"):
        this_week()
    if (sys.argv[1] == "fence"):
        fence()


'''
To do:
    - integrate with an SQL database, make the comment feature better.
    - Add in a thing about weekly estimates.

Foundations         9 = 1.5x3 = 4.5 hours of classes, 4.5 hours of homework
Syntactic Theory    6 = 1.5x2 = 3 hours of classes, 3 hours of homework
CL4LRL              7 = 1.5 = 5.5 hours of homework
Stats. in Ling.     (3)
PSR                 6 = 1.5x2 = 3 hours of class, 3 hours of homework

In total, that makes for 4.5+3+1.5+3 = 12 hours of class a week.
Homework = 4.5+3+5.5+3 = 15 hours of homework a week.

Uni: 28pw
Hiwi: 14pw

Total: 42pw

8.4 hours per day.
(Incidentally, if this is fillowed, there's no work on
weekends, even for hiwi. That's 168 minutes a day for hiwi.)

That's an 8 hour workday, which isn't so hard. 8:30-6:30 is a ten hour day. So, you have two spare hours

'''

