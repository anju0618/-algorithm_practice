def min_interval(intervals: list[list[int]], queries: list[int]) -> list[int]:
    result = []
    for q in queries:
        best = -1
        for start, end in intervals:
            if start <= q <= end:
                size = end - start + 1
                if best == -1 or size < best:
                    best = size
        result.append(best)
    return result
