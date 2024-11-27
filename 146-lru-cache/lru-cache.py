class LRUCache:
    from collections import OrderedDict

    def __init__(self, capacity: int):
        self.__capacity = capacity
        self.__cache = OrderedDict()

    def get(self, key: int) -> int:
        if key in self.__cache:
            self.__cache.move_to_end(key)
            return self.__cache[key]
        else:
            return - 1

    def put(self, key: int, value: int) -> None:
        if key in self.__cache:
            self.__cache.move_to_end(key)
        self.__cache[key] = value
        if len(self.__cache) > self.__capacity:
            self.__cache.popitem(last = False)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)