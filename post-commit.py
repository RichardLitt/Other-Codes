#!/usr/bin/env python
#####################
# This is a simple post to Twitter script that finds
# the most recent commit in the current repo. It will
# look for a URL - either for the website if the repo
# is a Github Pages repository, or for the URL for the
# repo in general to append to the tweet. 
# 
# Set the Environmental variables in your .bash_profile
# before trying to run it. You can get these keys from
# Twitter. 
#####################


import subprocess
import tweepy
import os

CONSUMER_KEY = os.environ['TWITTER_CONSUMER_KEY']
CONSUMER_SECRET = os.environ['TWITTER_CONSUMER_SECRET']
ACCESS_KEY = os.environ['TWITTER_ACCESS_KEY']
ACCESS_SECRET = os.environ['TWITTER_ACCESS_SECRET']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
cmd = [ 'git', 'log', '--pretty=format:%s', '-n1' ]
output = subprocess.Popen( cmd, stdout=subprocess.PIPE ).communicate()[0]
cmd = ['git', 'config', '--get', 'remote.origin.url']
origin = subprocess.Popen( cmd, stdout=subprocess.PIPE ).communicate()[0]
type_of_repo = origin.split(':')
tlds = ['.com', '.org', '.io']
if type_of_repo[0] == 'git@github.com':
  repo = type_of_repo[1].rstrip('.git\n')
  is_website = False
  for tld in tlds:
    if repo.split(tld)[-1] == '':
      repo = repo.split('/')[1]
      is_website = True
      break
  if not is_website:
    repo = 'https://github.com/' + repo;
elif type_of_repo[0] == 'https':
  repo = origin.strip('.git\n')
  for tld in tlds:
    if repo.split(tld)[-1] == '':
      repo = repo.split('/')[-1]
output = output + ' ' + repo
print output
#api.update_status(output)
