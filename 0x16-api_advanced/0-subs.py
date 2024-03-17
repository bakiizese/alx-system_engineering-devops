#!/usr/bin/python3
'''try reddit'''

def number_of_subscribers(subreddit):
    '''redit'''
    import requests

    red = requests.get("https://www.reddit.com/r/{}/about.json"
                            .format(subreddit),
                            headers={"User-Agent": "User-Agent"},
                            allow_redirects=False)
    if red.status_code != 200:
        return 0

    return red.json().get("data").get("subscribers")
