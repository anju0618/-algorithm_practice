def find_kth_largest(nums: list[int], k: int) -> int:
    heap = []  # サイズkのmin-heap: 一番小さい値がk番目に大きい値

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

    for n in nums:
        push(n)
        if len(heap) > k:
            pop()
    return heap[0]
