#!/usr/bin/python3
"""Import from the Parent class BaseCaching"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """LIFOCache class that inherits from BaseCaching"""

    def __init__(self):
        """Initialize LIFOCache"""
        self.stack = []
        super().__init__()

    def put(self, key, item):
        """Add the item to the dictionary"""
        if key and item:
            if self.cache_data.get(key):
                self.stack.remove(key)
            while len(self.stack) >= self.MAX_ITEMS:
                # If cache is full, discard the last item (LIFO)
                delete = self.stack.pop() # Delete the last item
                self.cache_data.pop(delete)
                print("DISCARD: {}".format(delete))
            self.stack.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """Return the value associated with the given key"""
        return self.cache_data.get(key)
