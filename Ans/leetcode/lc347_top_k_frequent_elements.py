def top_k_frequent(nums: list[int], k: int) -> list[int]:
    counts = {}
    for n in nums:
        counts[n] = counts.get(n, 0) + 1

    max_count = 0
    for c in counts.values():
        if c > max_count:
            max_count = c

    # バケツソート: buckets[c] = 出現回数がちょうどcの値のリスト
    buckets = [[] for _ in range(max_count + 1)]
    for n, c in counts.items():
        buckets[c].append(n)

    result = []
    for c in range(max_count, 0, -1):
        for n in buckets[c]:
            result.append(n)
            if len(result) == k:
                return result
    return result
