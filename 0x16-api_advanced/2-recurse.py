#!/usr/bin/python3
'''recurse api'''
import requests


after = None
def recurse(subreddit, hot_list=[]):
    '''recurse through reddit'''
    
    global after
    user_agent = {'User-Agent': 'api_advanced'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    parameters = {'after': after}
    results = requests.get(url, params=parameters, headers=user_agent,
                           allow_redirects=False)
    if results.status_code == 200:
        af_data = results.json().get("data").get("after")
        if af_data is not None:
            after = af_data
            recurse(subreddit, hot_list)
        titles = results.json().get("data").get("children")
        for tit in titles:
            hot_list.append(tit.get("data").get("title"))
        return hot_list
    else:
        return (None)