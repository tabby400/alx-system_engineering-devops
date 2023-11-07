#!/usr/bin/python3
"""printing the  first 10 hot posts on a subreddit"""

import requests


def top_ten(subreddit):
    """this function queries the reddit API and prints the
        titles of the first 10 hot posts in reddit"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        for h in range(10):
            print(posts[h]['data']['title'])
    else:
        print(None)
