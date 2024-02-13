#!/usr/bin/python3
'''reddit api'''
import requests


def number_of_subscribers(subreddit):
    '''return the total number of subscribers in a given subreddit'''
    if (subreddit is None or type(subreddit) is not str):
        return 0
    redit = requests.get(url='https://www.reddit.com/r/{}/\
                             about.json'.format(subreddit))
    if (redit.status_code == 200):
        redit = redit.json()
        j = redit['data']['subscribers']
        return j
    else:
        return 0
