def last_stone_weight(stones: list[int]) -> int:
    heap = [-s for s in stones]  # 負の値にしてmin-heapをmax-heap代わりに使う

    def sift_down(start, size):
        i = start
        while True:
            left, right, smallest = 2 * i + 1, 2 * i + 2, i
            if left < size and heap[left] < heap[smallest]:
                smallest = left
            if right < size and heap[right] < heap[smallest]:
                smallest = right
            if smallest == i:
                break
            heap[i], heap[smallest] = heap[smallest], heap[i]
            i = smallest

    n = len(heap)
    for i in range(n // 2 - 1, -1, -1):
        sift_down(i, n)

    def push(val):
        heap.append(val)
        i = len(heap) - 1
        while i > 0:
            parent = (i - 1) // 2
            if heap[parent] <= heap[i]:
                break
            heap[parent], heap[i] = heap[i], heap[parent]
            i = parent

    def pop():
        top = heap[0]
        last = heap.pop()
        if heap:
            heap[0] = last
            sift_down(0, len(heap))
        return top

    while len(heap) > 1:
        y = -pop()
        x = -pop()
        if y != x:
            push(-(y - x))

    return -heap[0] if heap else 0
