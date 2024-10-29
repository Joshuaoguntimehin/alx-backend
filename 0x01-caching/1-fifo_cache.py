#!/usr/bin/python3
"""import statement"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    def __init(self):
        """Initialize  the parent class's init"""
        super().__init__()

    def put(self, key, item):
        if key is None or item is None:
            return
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key = next(iter(self.cache_data))
            print(f'DISCARD:{first_key}')

        self.cache_data[key] = item

    def get(self, key):
        if key is None:
            return None
        return self.cache_data.get((key))
