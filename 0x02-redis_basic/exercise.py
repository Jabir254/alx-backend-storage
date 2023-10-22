#!/usr/bin/env python3
'''Writitng strings to Redis'''

import redis
import uuid
from typing import Union


class Cache:
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        # Generate a random key using uuid
        random_key = str(uuid.uuid4())

        # Store the data in Redis using the random key
        if isinstance(data, (int, float)):
            # If data is an int or float, store it as a string
            data = str(data)
        self._redis.set(random_key, data)

        # Return the generated key
        return random_key
