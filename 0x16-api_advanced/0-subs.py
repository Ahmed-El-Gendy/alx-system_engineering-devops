#!/usr/bin/python3
"""Queries the Reddit API"""


def number_of_subscribers(subreddit):
    """number_of_subscribers"""
    import requests

    sub_info = requests.get("https://www.reddit.com/r/{}/about.json"
                            .format(subreddit),
                            headers={"User-Agent": "My-User-Agent"},
                            allow_redirects=False)
    if sub_info.status_code >= 300:
        return 0

    return response.json().get("data").get("subscribers")
