#!/usr/bin/python3
"""Queries the Reddit API"""


def top_ten(subreddit):
    """top 10 hot posts"""
    import requests

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers,
                            allow_redirects=False)
    if response.status_code >= 300:
        print("None")
    else:
        for post in response.json().get("data").get("children"):
            print(post.get("data").get("title"))