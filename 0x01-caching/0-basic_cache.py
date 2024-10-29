#!/usr/bin/env python3
"""
BasicCashing module
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    defines a basic caching system without any limit
    """
    def put(self, key, item):
        """assign to the dictionary"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """return the value"""
        if key is None:
            return None
        return (self.cache_data[key])
