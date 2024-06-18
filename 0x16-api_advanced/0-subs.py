#!/usr/bin/python3
import requests

'''
Queries the Reddit API and returns the number of subscribers
'''


def number_of_subscribers(subreddit):
    '''
    number_of_subscribers
    '''

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data["data"]["subscribers"]
    else:
        return 0
