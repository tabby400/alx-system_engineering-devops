#!/usr/bin/python3
"""the function is sending a query to the Reddit API
 to return the number of subscribers"""


import requests


def number_of_subscribers(subreddit):
    """ the number of subscribers are returned"""
    headers = {"User-Agent": 'my_bot/0.0.1'}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()  # in json format
        return data["data"]["subscribers"]
    else:
        return 0
