#!/usr/bin/python3
"""import statement"""
from base_caching import BaseCaching
class MRUCache(BaseCaching):
    def __init__(self):
        super().__init__()
        self.order = [] 
    
    def put(self, key, item):
        if key is None or item is None:
            return

        # Add or update the cache and track the order
        self.cache_data[key] = item
        if key in self.order:
            self.order.remove(key)
        self.order.append(key)

        # If the cache exceeds the limit, discard the most recently used item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            mru_key = self.order.pop()  # Most recently used item to be discarded
            del self.cache_data[mru_key]
            print(f"DISCARD: {mru_key}")
    
    def get(self, key):        
        if key is None or key not in self.cache_data:
            return None
        
        self.order.remove(key)
        self.order.append(key)

        return self.cache_data[key]