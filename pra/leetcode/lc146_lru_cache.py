class LRUCache:
    def __init__(self, capacity: int):
        # TODO: implement (hash map + doubly linked list, no collections.deque)
        pass

    def get(self, key: int) -> int:
        pass

    def put(self, key: int, value: int) -> None:
        pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    check("get 1", cache.get(1), 1)
    cache.put(3, 3)  # evicts key 2
    check("2 was evicted", cache.get(2), -1)
    cache.put(4, 4)  # evicts key 1
    check("1 was evicted", cache.get(1), -1)
    check("3 still present", cache.get(3), 3)
    check("4 still present", cache.get(4), 4)
