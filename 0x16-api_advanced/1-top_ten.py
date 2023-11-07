#!/usr/bin/python3
"""printing the  first 10 hot posts on a subreddit"""

import requests


def top_ten(subreddit):
    """this function queries the reddit API and prints the
        titles of the first 10 hot posts in reddit"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        response = requests.get(url, headers=headers,
                                allow_redirects=False)
        if response.status_code == 200:
            children = response.json().get('data').get('children')
            for k in range(10):
                print(children[k].get('data').get('title'))
        else:
            print("None")
    except Exception:
        print("None")  # if issues with http requests
