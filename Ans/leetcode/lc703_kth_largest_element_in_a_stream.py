class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.heap = []  # サイズkのmin-heap: 一番小さい値がheap[0]、それがk番目に大きい値
        for n in nums:
            self.add(n)

    def _push(self, val: int) -> None:
        self.heap.append(val)
        i = len(self.heap) - 1
        while i > 0:
            parent = (i - 1) // 2
            if self.heap[parent] <= self.heap[i]:
                break
            self.heap[parent], self.heap[i] = self.heap[i], self.heap[parent]
            i = parent

    def _pop(self) -> int:
        top = self.heap[0]
        last = self.heap.pop()
        if self.heap:
            self.heap[0] = last
            i, n = 0, len(self.heap)
            while True:
                left, right, smallest = 2 * i + 1, 2 * i + 2, i
                if left < n and self.heap[left] < self.heap[smallest]:
                    smallest = left
                if right < n and self.heap[right] < self.heap[smallest]:
                    smallest = right
                if smallest == i:
                    break
                self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
                i = smallest
        return top

    def add(self, val: int) -> int:
        self._push(val)
        if len(self.heap) > self.k:
            self._pop()
        return self.heap[0]
