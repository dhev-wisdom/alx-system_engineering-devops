#!/usr/bin/python3
"""
Module queries the Reddit API
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Function to that queries Reddit API and returns list of hot post titles
    in several pages
    """
    url = ("https://www.reddit.com/r/{}/hot.json"
           "?after={}".format(subreddit, after))
    headers = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64)"}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        resp_json = response.json()
        for children in resp_json.get("data").get("children"):
            hot_list.append(children.get("data").get("title"))
        after = resp_json.get("data").get("after")
        if not after:
            return hot_list
        return recurse(subreddit, hot_list, after)

    else:
        return None
