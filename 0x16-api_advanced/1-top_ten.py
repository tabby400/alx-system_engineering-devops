#!/usr/bin/python3
"""printing the  first 10 hot posts on a subreddit"""

import requests


def top_ten(subreddit):
    """this  to get the first 10 post of a given sub reddit"""
    headers = {"User-Agent": "Kimanisamson"}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        custom_post = data['data']['children']
        for p in range(10):
            print(custom_post[p]['data']['title'])
    else:
        print(None)
