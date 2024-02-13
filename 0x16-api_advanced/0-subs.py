from requests import get


def number_of_subscribers(subreddit):
    if subreddit is None or not isinstance(subreddit, str):
        return 0

    #user_agent = {'User-agent': 'Google Chrome Version 81.0.4044.129'}
    head = {'User-Agent': 'My User Agent 1.0'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = get(url, headers=head)

    try:
        response.raise_for_status()  # Raise an exception for HTTP errors
        results = response.json()
        return results.get('data', {}).get('subscribers', 0)
    except Exception as e:
        print(f"Error: {e}")
        return 0
