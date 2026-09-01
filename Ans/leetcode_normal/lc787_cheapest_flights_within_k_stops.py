def find_cheapest_price(n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
    inf = float("inf")
    dist = [inf] * n
    dist[src] = 0

    # ベルマン・フォード法をk+1回だけ緩和する（「stopの数」を回数で制御する）
    for _ in range(k + 1):
        new_dist = dist[:]
        for u, v, w in flights:
            if dist[u] != inf and dist[u] + w < new_dist[v]:
                new_dist[v] = dist[u] + w
        dist = new_dist

    return dist[dst] if dist[dst] != inf else -1
