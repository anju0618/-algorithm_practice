def k_closest(points: list[list[int]], k: int) -> list[list[int]]:
    heap = []  # サイズkのmax-heap (距離の負数, 点) を保持

    def push(item):
        heap.append(item)
        i = len(heap) - 1
        while i > 0:
            parent = (i - 1) // 2
            if heap[parent][0] <= heap[i][0]:
                break
            heap[parent], heap[i] = heap[i], heap[parent]
            i = parent

    def pop():
        top = heap[0]
        last = heap.pop()
        if heap:
            heap[0] = last
            i, n = 0, len(heap)
            while True:
                left, right, smallest = 2 * i + 1, 2 * i + 2, i
                if left < n and heap[left][0] < heap[smallest][0]:
                    smallest = left
                if right < n and heap[right][0] < heap[smallest][0]:
                    smallest = right
                if smallest == i:
                    break
                heap[i], heap[smallest] = heap[smallest], heap[i]
                i = smallest
        return top

    for x, y in points:
        dist_sq = x * x + y * y
        push((-dist_sq, [x, y]))  # 負にしてmin-heapでmax-heap扱いにする
        if len(heap) > k:
            pop()

    return [item[1] for item in heap]
