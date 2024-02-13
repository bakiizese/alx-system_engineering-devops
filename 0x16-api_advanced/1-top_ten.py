#!/usr/bin/python3
'''top ten titles'''
import requests


def top_ten(subreddit):
    '''top ten'''

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'api_advanced'}
    reddit = requests.get(url, headers=headers,
                          allow_redirects=False)
    if reddit.status_code == 200:
        dicts = reddit.json().get('data').get('children')
        for i in range(10):
            print(dicts[i].get('data').get('title'))
    else:
        print("None")
