def network_delay_time(times: list[list[int]], n: int, k: int) -> int:
    graph = {i: [] for i in range(1, n + 1)}
    for u, v, w in times:
        graph[u].append((v, w))

    dist = {i: float("inf") for i in range(1, n + 1)}
    dist[k] = 0

    heap = [(0, k)]  # 手書きmin-heap: (現在までの最短距離, ノード)

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

    visited = {}
    while heap:
        d, node = pop()
        if node in visited:
            continue
        visited[node] = True
        for neighbor, weight in graph[node]:
            nd = d + weight
            if nd < dist[neighbor]:
                dist[neighbor] = nd
                push((nd, neighbor))

    result = 0
    for i in range(1, n + 1):
        if dist[i] == float("inf"):
            return -1
        if dist[i] > result:
            result = dist[i]
    return result
