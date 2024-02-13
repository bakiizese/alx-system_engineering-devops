#!/usr/bin/python3
'''top ten titles'''
import requests

def top_ten(subreddit):
    '''top ten'''

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'api_advanced'}
    response = requests.get(url, headers=headers,
                                allow_redirects=False)
    if response.status_code == 200:
        children = response.json().get('data').get('children')
        for i in range(10):
            print(children[i].get('data').get('title'))
    else:
        print("None")
