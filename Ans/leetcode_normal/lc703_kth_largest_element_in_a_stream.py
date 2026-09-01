class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.sorted_vals = []  # 昇順に保った、直近k個までの値
        for n in nums:
            self.add(n)

    def add(self, val: int) -> int:
        i = 0
        while i < len(self.sorted_vals) and self.sorted_vals[i] < val:
            i += 1
        self.sorted_vals.insert(i, val)
        if len(self.sorted_vals) > self.k:
            self.sorted_vals.pop(0)
        return self.sorted_vals[0]
