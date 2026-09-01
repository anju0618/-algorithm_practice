def network_delay_time(times: list[list[int]], n: int, k: int) -> int:
    graph = {i: [] for i in range(1, n + 1)}
    for u, v, w in times:
        graph[u].append((v, w))

    dist = {i: float("inf") for i in range(1, n + 1)}
    dist[k] = 0
    visited = {}

    for _ in range(n):
        # 未確定のノードの中で距離最小のものを毎回線形探索で選ぶ（heapqは使わない）
        current = None
        for node in range(1, n + 1):
            if node in visited:
                continue
            if current is None or dist[node] < dist[current]:
                current = node
        if current is None or dist[current] == float("inf"):
            break
        visited[current] = True
        for neighbor, weight in graph[current]:
            nd = dist[current] + weight
            if nd < dist[neighbor]:
                dist[neighbor] = nd

    result = 0
    for i in range(1, n + 1):
        if dist[i] == float("inf"):
            return -1
        if dist[i] > result:
            result = dist[i]
    return result
