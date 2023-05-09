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
            "User-Agent": "Ubuntu; Linux x86_64; Firefox/89.0"
            }

    response = requests(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        results = response.json().get("data")
        return results.get("subscribers")

    return 0
