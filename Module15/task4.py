# Кэширование запросов
from typing import Any


class LRUCache:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.cache_dict = {}
        self.cache_order = []

    @property
    def cache(self) -> Any:
        if len(self.cache_order) > 0:
            oldest_key = self.cache_order[0]
            return (oldest_key, self.cache_dict[oldest_key])
        else:
            return None

    @cache.setter
    def cache(self, new_elem: tuple[Any, Any]) -> None:
        key, value = new_elem
        if key in self.cache_dict:
            self.cache_order.remove(key)
        elif len(self.cache_dict) >= self.capacity:
            oldest_key = self.cache_order.pop(0)
            del self.cache_dict[oldest_key]

        self.cache_dict[key] = value
        self.cache_order.append(key)

    def get(self, key: Any) -> Any:
        if key in self.cache_dict:
            self.cache_order.remove(key)
            self.cache_order.append(key)
            return self.cache_dict[key]
        else:
            return None

    def print_cache(self) -> None:
        print("LRU Cache:")
        for key in self.cache_order:
            print(f"{key} : {self.cache_dict[key]}")


cache = LRUCache(3)
cache.cache = ("key1", "value1")
cache.cache = ("key2", "value2")
cache.cache = ("key3", "value3")
cache.print_cache()
print(cache.get("key2"))
cache.cache = ("key4", "value4")
cache.print_cache()