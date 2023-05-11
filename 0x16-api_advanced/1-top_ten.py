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
    headers = {"Mozilla/5.0 (X11; Ubuntu; Linux x86_64i"}
    params = {"limit": 10} 

    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code == 200:
        results = response.json().get("data")
        
        for post in results.get("children"):
            print(post.get("data").get("title"))

    else:
        print(None)
