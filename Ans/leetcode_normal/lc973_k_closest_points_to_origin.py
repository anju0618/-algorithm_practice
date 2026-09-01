def k_closest(points: list[list[int]], k: int) -> list[list[int]]:
    ranked = []  # (原点からの距離の2乗, 点) を昇順に保つ
    for x, y in points:
        dist_sq = x * x + y * y
        i = 0
        while i < len(ranked) and ranked[i][0] < dist_sq:
            i += 1
        ranked.insert(i, (dist_sq, [x, y]))
    return [point for _, point in ranked[:k]]
