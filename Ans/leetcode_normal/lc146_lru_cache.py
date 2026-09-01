class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # 普通のdictは挿入順を保持する。先頭=最も長く未使用、末尾=最近使った

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        value = self.cache[key]
        del self.cache[key]
        self.cache[key] = value  # 末尾に移動させる = 最近使ったことにする
        return value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            del self.cache[key]
        self.cache[key] = value

        if len(self.cache) > self.capacity:
            oldest_key = next(iter(self.cache))  # 先頭 = 最も長く未使用のキー
            del self.cache[oldest_key]
