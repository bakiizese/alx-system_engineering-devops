#!/usr/bin/python3
'''recurse'''
import requests


def count_words(subreddit, word_list, new_after='', words_dict={}):
    '''recurse count'''
    word_list = [word.lower() for word in word_list]

    res = requests.get(f"https://www.reddit.com/r/{subreddit}/hot.json",
                       headers={'User-Agent': 'api_advanced'},
                       params={'after': new_after},
                       allow_redirects=False)
    
    if res.status_code != 200:
        return

    try:
        response = res.json().get('data', None)
        if response is None:
            return
    except ValueError:
        return

    children = response.get('children', [])

    for post in children:
        title = post.get('data', {}).get('title', '')
        for key_word in word_list:
            for word in title.lower().split():
                if key_word == word:
                    words_dict[key_word] = words_dict.get(key_word, 0) + 1

    new_after = response.get('after', None)

    if new_after is None:
        sorted_dict = sorted(words_dict.items(),
                             key=lambda x: x[1],
                             reverse=True)

        for key, value in sorted_dict:
            if value != 0:
                print(f"{key}: {value}")
        return

    return count_words(subreddit, word_list, new_after, words_dict)