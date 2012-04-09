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
"Anchorman",
"The English Patient",
"Thank You for Smoking",
"Syriana",
"Dead Poets Society"]

import random
import sys
import os
#print(os.environ['PATH'])

#has_movies = os.system('ls /Users/richardlittauer/Movies')
#has_series = os.system('ls /Users/richardlittauer/Movies')

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

def pikachu():
    choice = dice()
    command = "VLC " + str(choice)
    #print command
    os.system(command)

if __name__ == "__main__":
    if (sys.argv[1] == "choose"):
        dice()
    if (sys.argv[1] == "pikachu"):
        pikachu()
'''
Things to do!
    - Make it automatically select movies based on what is in the folder?
    - Make it move files out of the folder when it has seen them.
'''
