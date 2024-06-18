#!/usr/bin/python3
"""Queries the Reddit API"""


def top_ten(subreddit):
    """top 10 hot posts"""
    import requests

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()
    except requests.exceptions.RequestException:
        print("None")
        return

    try:
        posts = response.json().get("data", {}).get("children", [])
        if not posts:
            print("None")
            return

        for post in posts:
            print(post.get("data", {}).get("title", ""))
    except (ValueError, KeyError):
        print("None")
