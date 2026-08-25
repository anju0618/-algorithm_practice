def min_interval(intervals: list[list[int]], queries: list[int]) -> list[int]:
    def insertion_sort_by_key(items, keyfunc):
        arr = list(items)
        for i in range(1, len(arr)):
            key_item = arr[i]
            key_val = keyfunc(key_item)
            j = i - 1
            while j >= 0 and keyfunc(arr[j]) > key_val:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key_item
        return arr

    sorted_intervals = insertion_sort_by_key(intervals, lambda x: x[0])
    indexed_queries = insertion_sort_by_key(list(enumerate(queries)), lambda x: x[1])

    result = [-1] * len(queries)
    heap = []  # (区間サイズ, 終端) の手書きmin-heap

    def push(item):
        heap.append(item)
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
            i, size = 0, len(heap)
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
        return top

    idx = 0
    n = len(sorted_intervals)
    for original_i, q in indexed_queries:
        while idx < n and sorted_intervals[idx][0] <= q:
            start, end = sorted_intervals[idx]
            push((end - start + 1, end))
            idx += 1
        while heap and heap[0][1] < q:
            pop()
        if heap:
            result[original_i] = heap[0][0]

    return result
