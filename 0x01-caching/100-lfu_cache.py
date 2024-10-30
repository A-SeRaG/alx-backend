#!/usr/bin/env python3
"""
LFUCache module
"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    def __init__(self):
        """Initialize the LFU cache"""
        super().__init__()
        self.usage_count = {}
        self.usage_order = []

    def put(self, key, item):
        """Add an item to the cache using LFU policy"""
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.usage_count[key] += 1
            self.usage_order.remove(key)
            self.usage_order.append(key)
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                min_frequency = min(self.usage_count.values())
                lfu_keys = [k for k, v in self.usage_count.items()
                            if v == min_frequency]

                if len(lfu_keys) > 1:
                    lfu_key = next(k for k in self.usage_order
                                   if k in lfu_keys)
                else:
                    lfu_key = lfu_keys[0]

                del self.cache_data[lfu_key]
                del self.usage_count[lfu_key]
                self.usage_order.remove(lfu_key)
                print(f"DISCARD: {lfu_key}")

            self.cache_data[key] = item
            self.usage_count[key] = 1
            self.usage_order.append(key)

    def get(self, key):
        """Get an item from the cache and update its usage frequency"""
        if key is None or key not in self.cache_data:
            return None

        self.usage_count[key] += 1
        self.usage_order.remove(key)
        self.usage_order.append(key)
        return self.cache_data[key]
