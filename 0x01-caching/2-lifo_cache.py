#!/usr/bin/python3
""" LIFOCache module """

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache is a caching system that follows the LIFO algorithm """

    def __init__(self):
        """ Initialize the cache """
        super().__init__()
        self.last_key = None  # To track the last added key

    def put(self, key, item):
        """ Add an item to the cache following LIFO policy """
        if key is not None and item is not None:
            self.cache_data[key] = item
            self.last_key = key  # Update the last added key

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                # LIFO: Discard the last inserted key
                del self.cache_data[self.last_key]
                print(f"DISCARD: {self.last_key}")

    def get(self, key):
        """ Get an item by key from the cache """
        return self.cache_data.get(key) if key is not None else None
