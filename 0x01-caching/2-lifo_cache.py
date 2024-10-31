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
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                oldkey = self.order.pop(3)
                del self.cache_data[oldkey]
                print(f"DISCARD: {oldkey}")
            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """Retrive value of the key"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
