class MedianFinder:
    def __init__(self):
        self.values = []  # 常にソート済みの状態を保つ

    def add_num(self, num: int) -> None:
        # 入れる位置を線形探索してから挿入する（挿入ソートと同じ考え方）
        i = 0
        while i < len(self.values) and self.values[i] < num:
            i += 1
        self.values.insert(i, num)

    def find_median(self) -> float:
        n = len(self.values)
        mid = n // 2
        if n % 2 == 1:
            return float(self.values[mid])
        return (self.values[mid - 1] + self.values[mid]) / 2
