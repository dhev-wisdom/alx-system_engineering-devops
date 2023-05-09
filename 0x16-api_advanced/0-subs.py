#!/usr/bin/python3
"""
Module queries the Reddit API
"""

import requests


def number_of_subscribers(subreddit):
    """
    Function to that queries Reddit API and returns the number of subscribers
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
            "User-Agent": "ubuntu:hbtn:v1.0 (by /u/piroli_)"
            }

    response = requests(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        results = response.json().get("data")
        return results.get("subscribers")

    return 0
