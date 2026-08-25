class MedianFinder:
    def __init__(self):
        self.small = []  # 前半分（小さい方）のmax-heap。負の値を入れてmin-heapを流用
        self.large = []  # 後半分（大きい方）のmin-heap

    def _push(self, heap, val):
        heap.append(val)
        i = len(heap) - 1
        while i > 0:
            parent = (i - 1) // 2
            if heap[parent] <= heap[i]:
                break
            heap[parent], heap[i] = heap[i], heap[parent]
            i = parent

    def _pop(self, heap):
        top = heap[0]
        last = heap.pop()
        if heap:
            heap[0] = last
            i, n = 0, len(heap)
            while True:
                left, right, smallest = 2 * i + 1, 2 * i + 2, i
                if left < n and heap[left] < heap[smallest]:
                    smallest = left
                if right < n and heap[right] < heap[smallest]:
                    smallest = right
                if smallest == i:
                    break
                heap[i], heap[smallest] = heap[smallest], heap[i]
                i = smallest
        return top

    def add_num(self, num: int) -> None:
        self._push(self.small, -num)
        moved = -self._pop(self.small)
        self._push(self.large, moved)

        if len(self.large) > len(self.small):
            moved = self._pop(self.large)
            self._push(self.small, -moved)

    def find_median(self) -> float:
        if len(self.small) > len(self.large):
            return float(-self.small[0])
        return (-self.small[0] + self.large[0]) / 2
