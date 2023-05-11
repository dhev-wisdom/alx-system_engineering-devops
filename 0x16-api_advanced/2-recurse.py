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
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64i)"}
    params = {"limit": 10}
    if after:
        params["after"] = after

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code == 200:
        results = response.json().get("data")
        children = results.get("children")
        if not children:
            return hot_list
        for child in children:
            hot_list.append(child.get("data").get("title"))
        return recurse(subreddit, hot_list=[], results.get("after"))

    else:
        return None
