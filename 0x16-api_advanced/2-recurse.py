#!/usr/bin/python3
"""Function queries a list of all hot posts on a subreddit."""
import requests


def recurse(subreddit, hot_lst=[], after="", count=0):
    """Returns listing of titles of all hot posts on a subreddit."""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
            "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/JojoBaPb)"
    }
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        return None

    results = response.json().get("data")
    after = results.get("after")
    count += results.get("dist")
    for c in results.get("children"):
        hot_lst.append(c.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_lst, after, count)
    return hot_lst
