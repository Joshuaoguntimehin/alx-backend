#!/usr/bin/python3
""" FIFOCache module """

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache is a caching system that follows the FIFO algorithm """

    def __init__(self):
        """ Initialize the cache """
        super().__init__()
        self.keys_order = []  # List to keep track of the insertion order

    def put(self, key, item):
        """ Add an item to the cache following FIFO policy """
        if key is not None and item is not None:
            if key not in self.cache_data:
                self.keys_order.append(key)

            self.cache_data[key] = item

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                # FIFO: Discard the first inserted key
                first_key = self.keys_order.pop(0)
                del self.cache_data[first_key]
                print(f"DISCARD: {first_key}")

    def get(self, key):
        """ Get an item by key from the cache """
        return self.cache_data.get(key) if key is not None else None

