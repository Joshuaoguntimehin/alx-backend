#!/usr/bin/python3
""" LRUCache module """

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ LRUCache is a caching system that follows the LRU algorithm """

    def __init__(self):
        """ Initialize the cache """
        super().__init__()
        self.access_order = []  # List to track the access order of keys

    def put(self, key, item):
        """ Add an item to the cache following LRU policy """
        if key is not None and item is not None:
            if key in self.cache_data:
                # If key already exists, remove it from the access order
                self.access_order.remove(key)

            # Add the key to the end (most recently used)
            self.access_order.append(key)
            self.cache_data[key] = item

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                # LRU: Remove the least recently used key (first in access_order)
                lru_key = self.access_order.pop(0)
                del self.cache_data[lru_key]
                print(f"DISCARD: {lru_key}")

    def get(self, key):
        """ Get an item by key from the cache and update access order """
        if key is None or key not in self.cache_data:
            return None

        # Update access order to reflect recent usage
        self.access_order.remove(key)
        self.access_order.append(key)

        return self.cache_data[key]
