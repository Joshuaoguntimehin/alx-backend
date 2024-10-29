#!/usr/bin/python3
"""import statement"""
from base_caching import BaseCaching

class LRUCache(BaseCaching):
    """LRUCache class that inherits from BaseCaching."""
    def __init__(self):
        """Initialize the class by calling the parent class initializer."""
        super().__init__()
        self.cache_data = OrderedDict()  # Use OrderedDict to maintain insertion order

    def put(self, key, item):
        """Assign the item to the key in the cache."""
        if key is None or item is None:
            return  # Do nothing if key or item is None

        # If the key already exists, remove it to update its position later
        if key in self.cache_data:
            self.cache_data.pop(key)

        # Add the key-value pair to the cache
        self.cache_data[key] = item

        # If the cache exceeds the max size, discard the least recently used item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # Discard the first item in the OrderedDict (LRU item)
            lru_key, _ = self.cache_data.popitem(last=False)
            print(f"DISCARD: {lru_key}")
        
    def get(self, key):
        """Retrieve the item linked to the key."""
        if key is None or key not in self.cache_data:
            return None  # Return None if key is invalid or not found

        # Move the accessed key to the end to mark it as recently used
        'BAQ,,,,'