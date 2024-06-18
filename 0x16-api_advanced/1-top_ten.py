#!/usr/bin/python3
"""Queries the Reddit API and prints the titles"""

import requests


def top_ten(subreddit):
    """Fetches and prints the titles of the top 10 hot posts"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()
    except requests.exceptions.RequestException:
        print("None")
        return

    try:
        data = response.json().get("data", {})
        children = data.get("children", [])

        if not children:
            print("None")
            return

        for post in children:
            print(post.get("data", {}).get("title", ""))
    except (ValueError, KeyError):
        print("None")
