#!/usr/bin/python3
"""Queries the Reddit API"""


def number_of_subscribers(subreddit):
    """number_of_subscribers"""
    import requests

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code >= 300:
        return 0

    return response.json().get("data").get("subscribers")
