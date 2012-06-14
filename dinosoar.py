"""
Scrape Dinosaur comics!
Developed by Richard L. with Ryan North's permission
"""

# These are packages
import urllib2 # Helps you open the url
from BeautifulSoup import BeautifulSoup #This is the parser/scraper/XMLer
import time # Used to be nice to the server
import datetime # Let's you access this package
import re # This is for regex

file = open('qwanto') # Open the file with the links you want to scrape

output_file_name = 'qwanto_scrape' # The name of the output file
#Open the file where you want to save stuff
output = open(output_file_name,'w+') 
# r+ = read it, add on the end. a = append, but doesn't read it, w+ means that
# you erase it each time, and then write it again. 

for line in file.readlines():
    u = urllib2.urlopen(line.strip()) #Access the server, gets html
    # mung it all together
    rawhtml = "".join(map(str.strip,u.readlines())) #Gets the html for real

    bs = BeautifulSoup(rawhtml).prettify()

    output.write(bs)

    #print the url
    print "\"" + line.strip() + "\","

    #Timestamp of scrape.
    print "\"" + str(datetime.datetime.now()) + "\","

    #print bs

    # Doesn't currently actually parse any of the XML. I'm getting there. 

    print
    time.sleep(1)

output.close()

