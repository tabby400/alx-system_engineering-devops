#!/usr/bin/python3

import requests
"""this recursive function queries the reddit api to return
list with title of all articles"""


def recurse(subreddit, hot_list=None, after=None):
    """function that getsa list of hot titles
    recursively"""
    
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
        "after": after,
        "count": 0,
        "limit": 100
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        return None

    results = response.json().get("data")
    after = results.get("after")
    count = count + results.get("dist")
    for h in results.get("children"):
        hot_list.append(h.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, outcome, count)
    return hot_list
