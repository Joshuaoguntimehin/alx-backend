#!/usr/bin/python3
"""IMPORT statement"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Return the value linked to key."""
        if key is None:
            return None
        return self.cache_data.get((key))
