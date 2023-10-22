#!/usr/bin/env python3
'''implementing an expiring web cache and tracker'''

import redis
import requests
from cachetools import TTLCache

cache = TTLCache(maxsize=100, ttl=10)


def get_page(url: str) -> str:
    # Check if the URL is already in the cache
    if url in cache:
        # Increment the access count for this URL
        cache[f'count:{url}'] += 1
        return cache[url]

    # Fetch the HTML content from the URL
    response = requests.get(url)
    html_content = response.text

    # Store the HTML content in the cache with the URL as the key
    cache[url] = html_content

    # Initialize or increment the access count for this URL
    if f'count:{url}' not in cache:
        cache[f'count:{url}'] = 1
    else:
        cache[f'count:{url}'] += 1

    return html_content
