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
import re
import dis

output_file_name = "oxygen_log.csv"

if (sys.argv[1] == "help"):
    print "-------------------Help Desk-------------------"
    print
    print "--begin <project> [last]/[%d | backtime]"
    print "--end <project> <\"comment\"> [%d | backtime]" 
    print "--status"
    print "--pause [%d | backtime]"
    print "--search <project> [print]"
    print "--hiwi [print]/[%d | total to work] "
    print "--today"
    print
    print "-----------------------------------------------"

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
    return output

if (sys.argv[1] == "begin"):
    f = open(output_file_name,'a')
    print "Mask on!"
    time_now = datetime.datetime.now()
    try:
        pattern = re.compile("\d+")
        match_o = re.match(pattern, sys.argv[3])
        if (match_o != None):
            today = datetime.datetime.now()
            min_change = datetime.timedelta(minutes=int(sys.argv[3]))
            time_adjust = today - min_change
            print "You have just adjusted time backwards: " + str(time_now) + " is now " + str(time_adjust) + "."
            time_now = time_adjust
    except: x = "There should be another option here."
    try:
        pattern = re.compile("last")
        match_o = re.match(pattern, sys.argv[3])
        if (match_o != None):
            f = open(output_file_name, 'r+')
            lineList = f.readlines()
            on = lineList[-1]
            pattern = re.compile("\d\d:\d\d:\d\d.\d+")
            match_o_time = re.search(pattern, on[27:])
            if (match_o_time != None):
                time_now = str(time_now)[:10] + " " + match_o_time.group(0)
                print "You have just adjusted your start level from the last known signal, at " + time_now + "."
    except: x = "This is a filler. You are in real time."
    f.write(str(time_now) + ", ")
    project = sys.argv[2]
    f.write(project + ", ")
    f.close()


if (sys.argv[1] == "end"):
    f = open(output_file_name, 'r+')
    lineList = f.readlines()
    on = lineList[-1]
    off = datetime.datetime.now()
    try:
        pattern = re.compile("\d+")
        match_o = re.match(pattern, sys.argv[4])
        if (match_o != None):
            today = datetime.datetime.now()
            min_change = datetime.timedelta(minutes=int(sys.argv[4]))
            time_adjust = today - min_change
            print "You have just adjusted time backwards: " + str(off) + " is now " + str(time_adjust) + "."
            off = time_adjust
    except:
        x = "This is a filler. You are in real time."
    off = str(off)
    from datetime import datetime
    FMT = '%H:%M:%S'
    tdelta = datetime.strptime(off[11:19], FMT) - datetime.strptime(on[11:19], FMT)
    total_time = str(tdelta)
    print 'Mask off!'
    print 'You were on the surface of Pandora from: ' + on[:19] + ' to ' + off[:19] + '.'
    time_labels = print_time_labels(total_time)
    print "You survived for %s." % time_labels
    comment = sys.argv[3]
    project = sys.argv[2]
    print 'Operation ' + project + ' is now terminated. Your activity report readout: '
    print comment
    f.write(str(off) + ", ")
    f.write(str(tdelta) + ", ")
    f.write(project + ", ")
    f.write(comment.replace("\"", "'"))
    f.write("\n")
    f.close()


if (sys.argv[1] == "status"):
    f = open(output_file_name, 'r')
    lineList = f.readlines()
    if lineList[-1][-2] != ",":
        f = open(output_file_name, 'r+')
        lineList = f.readlines()
        on = lineList[-1]
        try:
            pattern_time = re.compile("\d\d:\d\d\:\d\d.\d+")
            match_o_time = re.search(pattern_time, on[29:])
            if (match_o_time != None):
                onn = match_o_time.group(0)
                off = str(datetime.datetime.now())
                from datetime import datetime
                FMT = '%H:%M:%S'
                time_since = datetime.strptime(off[11:19], FMT) - datetime.strptime(onn[:8], FMT)
                time_since = str(time_since)
        except: x = "I am a whale"
        time_labels = print_time_labels(time_since)
        print "You have not been working for %s. Last job:" % time_labels
        print on
        if len(time_since) >= 10:
            print "Good morning. You haven't started working yet today."
            print "Your last read out was: " + on.replace("\n","")
    if len(lineList[-1]) <= 40:
        on = lineList[-1]
        last_job = on[28:].replace(",", "").replace(" ", "")
        off = str(datetime.datetime.now())
        from datetime import datetime
        FMT = '%H:%M:%S'
        tdelta = datetime.strptime(off[11:19], FMT) - datetime.strptime(on[11:19], FMT)
        on = lineList[-1].replace(", ", ". Your current Operation: ").replace(",", ".")
        print 'You are currently on project \'' + last_job + '\' in Pandora. Your last signal was at ' + on[:19] + '. Time alive: ' + str(tdelta) + '.'
    f.close()


if (sys.argv[1] == "pause"):
    f = open(output_file_name, 'r+')
    lineList = f.readlines()
    on = lineList[-1]
    off = datetime.datetime.now()
    try:
        pattern = re.compile("\d+")
        match_o = re.match(pattern, sys.argv[2])
        if (match_o != None):
            today = datetime.datetime.now()
            min_change = datetime.timedelta(minutes=int(sys.argv[2]))
            time_adjust = today - min_change
            print "You have just adjusted time backwards: " + str(off) + " is now " + str(time_adjust) + "."
            off = time_adjust
    except:
        x = "This is a filler. You are in real time."
    off = str(off)
    from datetime import datetime
    FMT = '%H:%M:%S'
    tdelta = datetime.strptime(off[11:19], FMT) - datetime.strptime(on[11:19], FMT)
    print 'Mask off! You were on the surface of Pandora from ' + on[:19] + ' to ' + off[:19] + ' and survived for ' + str(tdelta) + '.'
    print 'What ho?! A break?'
    f.write(str(off) + ", ")
    f.write(str(tdelta) + ", ")
    f.write("Paused.")
    f.write("\n")
    f.close()


if (sys.argv[1] == "search"):
    f = open(output_file_name, 'r+')
    lineList = f.readlines()
    from datetime import datetime
    from datetime import timedelta
    total_time = "00:00:00"
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
                    print line.replace("\n", "")
            except: x = "This is a filler."
    print total_time
    f.close()


if (sys.argv[1] == "hiwi"):
    f = open(output_file_name, 'r+')
    lineList = f.readlines()
    from datetime import datetime
    from datetime import timedelta
    time_now = datetime.now()
    total_time = "00:00:00"
    total_time_today = "00:00:00"
    for line in lineList:
        pattern = re.compile("hiwi")
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
                    if (sys.argv[2] == "print"):
                        print line.replace("\n", "")
                except: x = "This is a filler."
            today_date = str(time_now)[:10]
            pattern_time = re.compile(str(today_date))
            match_o_time = re.match(pattern_time, line)
            if (match_o_time != None):
                if str(match_o_time.group(0))[:9] == str(time_now)[:9]:
                    pattern_time = re.compile("\d+\:\d\d\:\d\d\,")
                    match_o_time = re.search(pattern_time, line)
                    if (match_o_time != None):
                        match_o_t = str(match_o_time.group(0)).replace(",", "")
                        FMT = '%H:%M:%S'
                        tt = datetime.strptime(match_o_t, FMT)
                        total_time_today = datetime.strptime(str(total_time_today), FMT) + timedelta(hours=tt.hour,minutes=tt.minute,seconds=tt.second)
                        total_time_today = str(total_time_today)[11:]
            if len(line) <= 40:
                on = lineList[-1]
                off = str(datetime.now())
                from datetime import datetime
                FMT = '%H:%M:%S'
                tdelta = datetime.strptime(off[11:19], FMT) - datetime.strptime(on[11:19], FMT)
                on = lineList[-1]
                FMT = '%H:%M:%S'
                tt = datetime.strptime(str(tdelta), FMT)
                total_time_today = datetime.strptime(str(total_time_today), FMT) + timedelta(hours=tt.hour,minutes=tt.minute,seconds=tt.second)
                total_time = datetime.strptime(str(total_time), FMT) + timedelta(hours=tt.hour,minutes=tt.minute,seconds=tt.second)  
                total_time = str(total_time)[11:]                
                total_time_today = str(total_time_today)[11:]
    began = datetime(2011, 11, 9, 0, 0, 0)
    time_now = datetime.now()
    difference = time_now - began
    weeks, days = divmod(difference.days, 7)
    week_string = "weeks"
    day_string = "days"
    if weeks == 1:
        week_string = "week"
    if days == 1:
        day_string = "day"
    hours_expected = difference.days * 2
    behind = hours_expected - int(total_time[:2]) - 1
    minutes_behind =  60 - int(total_time[3:5])
    if int(total_time_today[:2]) == 1:
        x = 60
    if int(total_time_today[:2]) == 0:
        x = 120
    if int(total_time_today[:2]) >= 2:
        x = int(total_time_today[:2]) * 60
    try:
        pattern = re.compile("\d+")
        match_o = re.match(pattern, sys.argv[2])
        if (match_o != None):
            x = int(match_o.group(0))
    except: x = x
    minutes_behind_today = x - int(total_time_today[3:5])
    tt_hours = total_time[:2]
    tt_minutes = total_time[3:5]
    pay = (int(tt_hours)*12) + float(int(tt_minutes))/60*12
    total_pay = hours_expected*12
    total_minutes_left = (behind*60) + minutes_behind
    if tt_minutes[0] == "0":
        tt_minutes = tt_minutes[1:]
    hour_string = "hours"
    minute_string = "minutes"
    if int(tt_hours) == 1:
        hour_string = "hour"
    if tt_minutes == 1:
        minute_string = "minute"
    if behind == 1:
        hour_string = "hour"
    if minutes_behind == 1:
        minute_string = "minute"
    ttt_hours = total_time_today[:2]
    if int(ttt_hours) != 0:
        ttt_hours = str(ttt_hours) + " hours and "
    if int(ttt_hours[:2]) == 1:
        ttt_hours = str(ttt_hours[1:2]) + " hour and "
    else: ttt_hours = ""
    ttt_minutes = total_time_today[3:5]
    if ttt_minutes[0] == "0":
        ttt_minutes = ttt_minutes[1:]
    f.close()
    print ""
    print "---------------------------------Hiwi Status---------------------------------"
    print "You have been on this project for %d %s and %d %s. " % (weeks, week_string, days, day_string) + "Expected work: " + str(hours_expected) + " hours."
    print "Actual work: %s %s and %s %s. " % (tt_hours, hour_string, tt_minutes, minute_string) + "You are behind by %d %s and %d %s." % (behind, hour_string, minutes_behind, minute_string)
    print "You have earned %s euro, instead of %s euro." % (pay, total_pay)
    print ""
    print "Today you have worked a total of %s%s minutes. You have %s left. (%s)" % (ttt_hours, ttt_minutes, minutes_behind_today, total_minutes_left)
    print "-----------------------------------------------------------------------------"
    print ""

if (sys.argv[1] == "today"):
    f = open(output_file_name, 'r')
    lineList = f.readlines()
    time_now = datetime.datetime.now()
    print  
    from datetime import datetime
    from datetime import timedelta
    total_time = "00:00:00"
    total_time_alt = "00:00:00"
    specific_job_catch = "empty"
    for line in lineList:
        line = line.replace('\n', '')
        today_date = str(time_now)[:10]
        pattern_time = re.compile(str(today_date))
        match_o_time = re.match(pattern_time, line)
        if (match_o_time != None):
            line  = line.split(', ')
            if len(line) == 3:
                on = lineList[-1]
                off = str(datetime.now())
                from datetime import datetime
                FMT = '%H:%M:%S'
                tdelta = datetime.strptime(off[11:19], FMT) - datetime.strptime(on[11:19], FMT)
                on = lineList[-1].replace(", ", ". Your current Operation: ").replace(",", ".")
                worked = str(tdelta)
                read_out = "Ongoing..."
            if len(line) > 3:
                worked = line[3]
                read_out = line[5]
            time_labels = print_time_labels(worked)
            print "%s for %s: %s" % (line[1], time_labels, read_out)
            FMT = '%H:%M:%S'
            try:
                if line[1] != "off":
                    tt = datetime.strptime(worked, FMT)
                    total_time = datetime.strptime(str(total_time), FMT) + timedelta(hours=tt.hour,minutes=tt.minute,seconds=tt.second)
                    total_time = str(total_time)[11:]
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
            if (line[1] != "admin") and (line[1] != "off") and (line[1] != "coding"):
                if sys.argv[2][0] == "-":
                    if (line[1] != sys.argv[2]):
                        FMT = '%H:%M:%S'
                        tdelta = datetime.strptime(total_time, FMT) - datetime.strptime(line[3], FMT)
                        total_time_alt = str(tdelta)
                    specific_job = sys.argv[2][1:]
                    specific_job_catch = "except"
    time_labels = print_time_labels(total_time)
    print "You have worked a total of %s today. " % time_labels
    if specific_job_catch == "except":
        time_labels = print_time_labels(total_time_alt)
        print "Of that, you did everything but %s for %s." % (specific_job, time_labels)
    if specific_job_catch == "only":
        time_labels = print_time_labels(total_time_alt)
        print "Of that, you did %s for %s." % (specific_job, time_labels)
    print



'''

To do:
    - review functions

'''
