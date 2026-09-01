def min_cost_connect_points(points: list[list[int]]) -> int:
    n = len(points)
    if n <= 1:
        return 0

    def dist(i, j):
        return abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])

    visited = [False] * n
    min_dist = [float("inf")] * n
    min_dist[0] = 0
    total = 0

    for _ in range(n):
        # 未訪問の中で最もコストが小さい点を選ぶ（線形探索、ヒープなし）
        u = -1
        for i in range(n):
            if not visited[i] and (u == -1 or min_dist[i] < min_dist[u]):
                u = i
        visited[u] = True
        total += min_dist[u]
        for v in range(n):
            if not visited[v]:
                d = dist(u, v)
                if d < min_dist[v]:
                    min_dist[v] = d

    return total
