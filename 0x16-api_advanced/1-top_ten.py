#!/usr/bin/python3
"""
Module queries the Reddit API
"""

import requests


def top_ten(subreddit):
    """
    Function to that queries Reddit API and returns top ten hot post titles
    """ 
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "ubuntu:hbtn:v1.0 (by /u/piroli_)"}
    params = {"limit": 10} 

    response = requests(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code == 200:
        results = response.json().get("data")
        
        for post in results.get("children"):
            print(post.get("data").get("title"))

    else:
        print(None)
