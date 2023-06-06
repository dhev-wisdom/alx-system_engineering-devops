#!/usr/bin/python3
"""
Module queries the Reddit API
"""

from collections import defaultdict
import requests


def count_words(subreddit, word_list, after=None, word_count=defaultdict(int)):
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

        for word in word_list:
            word = word.lower()

        for children in resp_json.get("data").get("children"):
            title = children.get("data").get("title")
            words = title.split()

            for word in words:
                word_lower = word.lower()
                if word_lower in word_list:
                    word_count[word_lower] += 1

        after = resp_json.get("data").get("after")

        if not after:
            _dict = dict(sorted(word_count.items(),
                         key=lambda x: (-x[1], x[0].lower())))
            sorted_dict = sorted(_dict.items())
            for word, count in sorted_dict:
                print(f"{word.lower()}: {count}")
            return
        return count_words(subreddit, word_list, after, word_count)

    else:
        return None
