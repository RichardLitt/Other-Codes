To_See = ["Flight of the Conchords",
"Iron man",
"All of the Father Ted episodes",
"The rest of Black Books",
"Casablanca",
"Three days of the condor", 
"The Science of Sleep",
"The Quiet Man", 
"Solaris",
"Star Trek",
"The English Patient",
"Syriana",
"Dead Poets Society"]

import random
import sys
import os
import subprocess, sys	
#print(os.environ['PATH'])

#has_movies = os.system('ls /Users/richardlittauer/Movies')
#has_series = os.system('ls /Users/richardlittauer/Movies')

# The following functions depend not upon an individual list of files, nor on
# having the same type of files in a mineable folder, but rather more than
# that.

# This needs to be redefined for each folder you're looking at.
folder = '/Volumes/ASUKA/Diaz/'

# This lists the folder - global is a bit of a hack, but hey, it works. 
def folders():
    global folder
    cmd = [ 'ls', folder]
    output = subprocess.Popen( cmd, stdout=subprocess.PIPE ).communicate()[0]
    return output

# sort() puts all of the files and folders in that folder in a list, and
# chooses a random one to select and run.
def sort(output):
    catalogue = []
    output = output.split('\n')
    for line in output: catalogue.append(line)
    choice = random.randrange(len(catalogue))
    return catalogue[choice]

# Let's open up that folder, or return it if it's just a top-level movie file.
def open_folder(choice):
    global folder
    folder = folder + choice
    if folder[-3:] == 'avi':
        return folder
    if folder[-3:] == 'mkv':
        return
    else:
        cmd = [ 'ls', folder ]
        output = subprocess.Popen( cmd, stdout=subprocess.PIPE ).communicate()[0]
        return output

# This opens up the file in the appropriate player, and should work well if it
# is in a folder or not. This is also the end of these functions. 
def open_file(choice):
    choice = choice.split('\n')
    for line in choice:
        global folder
        line = folder + '/' + line
        print line
        line = line.replace(' ', '\ ').replace('(', '\(')\
                .replace(')','\)')
        if line[-4:] == '.avi':
            cmd = 'vlc ' + line
            os.system(str(cmd))
        if line[-4:] == '.mp4':
            cmd = 'open ' + line
            os.system(str(cmd))
        if line[-4:] == '.mkv':
            cmd = 'open ' + line
            os.system(str(cmd))

# This is another random sorter, but is a bit primitive and depends upon
# preloading in the movies you want to see. Thankfully, we're past this now. 
def dice():
    if sys.argv[2] == "movie":
        #choice = random.randrange(len(has_movies))
        t = os.system('ls /Users/richardlittauer/Movies')
        print t
        #return has_movies[choice]
    #if sys.argv[2] == "episode":
    #    choice = random.randrange(len(has_series))
    #    print has_series[choice]
    #    return has_series[choice]

# What is this I don't even
def pikachu():
    choice = dice()
    command = "VLC " + str(choice)
    #print command
    os.system(command)

# The main. Not, in fact, the Spanish main. 
if __name__ == "__main__":
    if (sys.argv[1] == "choose"):
        dice()
    if (sys.argv[1] == "pikachu"):
        pikachu()
    if (sys.argv[1] == 'Diaz'):
        open_file(open_folder(sort(folders())))

# Don't you just love comments?

'''
Things to do!
    - Make it move files out of the folder when it has seen them.
        - this would be awesome. 
'''
