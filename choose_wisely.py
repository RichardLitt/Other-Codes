# This is a movie chooser, for when you're too lazy or have too many movies and
# really can't decide what to pick. Choose wisely, or you'll turn into a Nazi
# skeleton and Elsa will die screaming.
#
# Developed and written by Richard Littauer.
# =============================================================================

# Some stuff that needs changing!

# For automatically getting the movies from a folder.
folder = '/Volumes/ASUKA/Diaz/'

# For preloading in the options, if you'd rather do that. 
has_movies = ["Iron man", "Casablanca", "Three days of the condor",  "The \
        Science of Sleep", "The Quiet Man",  "Solaris", "Star Trek", "The \
        English Patient", "Syriana", "Dead Poets Society"]

has_episodes = ['Flight of the Conchords', 'Father Ted', 'Spaced']


# =============================================================================

import random
import sys
import os
import subprocess	
#print(os.environ['PATH']) # Checks the current Path

# =============================================================================
# The following functions depend not upon an individual list of files, nor on
# having the same type of files in a mineable folder, but rather more than
# that.

### Note: It would be a lot easier to use:
# find . -name "*.avi" -print
# find . -name "*.mp4" -print
# find . -name "*.mkv" -print
# find . -name "*.AVI" -print
### Going to need to remove all *sample* files
### And work for CD1, CD2 entries. 

# This lists the folder - global is a bit of a hack, but hey, it works. 
def folders():
    global folder
    cmd = [ 'ls', folder ]
    output = subprocess.Popen(cmd, stdout=subprocess.PIPE).communicate()[0]
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
        return
    if folder[-3:] == 'mkv':
        return
    else:
        cmd = [ 'ls', folder ]
        output = subprocess.Popen(cmd, stdout=subprocess.PIPE).communicate()[0]
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


# =============================================================================
# This is another random sorter, but is a bit primitive and depends upon
# preloading in the movies you want to see. Thankfully, we're past this now. 
def dice():
    if sys.argv[2] == "movie":
        choice = random.randrange(len(has_movies))
        return has_movies[choice]
    if sys.argv[2] == "episode":
        choice = random.randrange(len(has_episodes))
        return has_episodes[choice]

# This actually plays the movie, if it's in the folder and titled
# appropriately.
def pikachu():
    choice = dice()
    choice = choice.replace(' ', '\ ').replace('(', '\(').replace(')', '\)')
    command = "VLC " + str(choice)
    os.system(command)


# =============================================================================
# The main. Not, in fact, the Spanish main. 
if __name__ == "__main__":
    # If you just want to pick from a random list
    if (sys.argv[1] == "choose"):
        dice()
    # If you want to try and run from that list
    if (sys.argv[1] == "pikachu"):
        pikachu()
    # If you just want a movie to run, period. No arguments, either.
    if (sys.argv[1] == 'Diaz'):
        open_file(open_folder(sort(folders())))

# Don't you just love comments?
