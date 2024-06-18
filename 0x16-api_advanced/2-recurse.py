#!/usr/bin/python3
"""Queries the Reddit API"""

import requests


def recurse(subreddit, hot_list=None, count=0, after=None):
    """Recursive function that queries the Reddit API"""
    if hot_list is None:
        hot_list = []

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    params = {"count": count, "after": after, "limit": 100}

    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)
        response.raise_for_status()
    except requests.exceptions.RequestException:
        return None

    try:
        data = response.json().get("data", {})
        children = data.get("children", [])
        hot_list += [post.get("data", {}).get("title", "")
                     for post in children]
        after = data.get("after")

        if not after:
            return hot_list

        return recurse(subreddit, hot_list, count + len(children), after)
    except (ValueError, KeyError):
        return None
