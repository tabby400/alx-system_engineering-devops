#!/usr/bin/python3
"""printing a sorted count of given keywords deliminated by space"""
import requests

def count_words(subreddit, word_list, results=None, after=None):
    if results is None:
        results = {}

    headers = {'User-Agent': 'python:reddit_api:1.0'}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    params = {'limit': 100, 'after': after}

    response = requests.get(url, headers=headers, params=params)

    if response.status_code != 200:
        return None

    data = response.json()['data']
    after = data['after']

    for post in data['children']:
        title = post['data']['title'].lower()

        for word in word_list:
            if title.count(word) > 0:
                if word in results:
                    results[word] += title.count(word)
                else:
                    results[word] = title.count(word)

    if after:
        return count_words(subreddit, word_list, results, after)

    # Sorting in descending order and then alphabetically
    sorted_results = sorted(results.items(), key=lambda x: (-x[1], x[0]))

    for word, count in sorted_results:
        print(f'{word}: {count}')

if __name__ == '__main__':
    subreddit = input("Enter subreddit: ")
    keywords = input("Enter keywords (space-separated): ").split()

    count_words(subreddit, keywords)
