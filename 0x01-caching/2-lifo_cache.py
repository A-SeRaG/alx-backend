#!/usr/bin/env python3
"""
LIFOCache module
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    Last input first output
    """
    def __init__(self):
        """Initialize class"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """Add item to the cashe using LIFO"""
        if key is not None and item is not None:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                if self.last_key:
                    del self.cache_data[self.last_key]
                    print(f"DISCARD: {self.last_key}")
        self.last_key = key

    def get(self, key):
        """Retrive value of the key"""
        return self.cache_data.get(key, None)
