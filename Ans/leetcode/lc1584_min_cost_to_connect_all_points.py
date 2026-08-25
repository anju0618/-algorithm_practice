def min_cost_connect_points(points: list[list[int]]) -> int:
    n = len(points)
    if n <= 1:
        return 0

    visited = [False] * n
    heap = [(0, 0)]  # (連結コスト, 点インデックス)

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
            i, size = 0, len(heap)
            while True:
                left, right, smallest = 2 * i + 1, 2 * i + 2, i
                if left < size and heap[left][0] < heap[smallest][0]:
                    smallest = left
                if right < size and heap[right][0] < heap[smallest][0]:
                    smallest = right
                if smallest == i:
                    break
                heap[i], heap[smallest] = heap[smallest], heap[i]
                i = smallest
        return top

    total = 0
    connected = 0
    while connected < n:
        cost, i = pop()
        if visited[i]:
            continue
        visited[i] = True
        total += cost
        connected += 1
        for j in range(n):
            if not visited[j]:
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                push((dist, j))

    return total
