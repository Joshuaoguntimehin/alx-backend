#!/usr/bin/python3
"""import statement"""
from base_caching import BaseCaching

class LIFOCache(BaseCaching):
    def __init__(self):
        super().__init__()
    
    def put(self, key, item):
        if key is None or item is None:
            return
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            last_key = next(reversed(self.cache_data))
            print(f'DISCARD: {last_key}')
            del self.cache_data[last_key]
            
        self.cache_data[key] = item

    def get(self, key):
        if key is None:
            return None
        return self.cache_data.get((key))