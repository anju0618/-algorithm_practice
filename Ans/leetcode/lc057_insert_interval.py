def insert(intervals: list[list[int]], new_interval: list[int]) -> list[list[int]]:
    result = []
    i = 0
    n = len(intervals)

    while i < n and intervals[i][1] < new_interval[0]:
        result.append(intervals[i])
        i += 1

    start, end = new_interval
    while i < n and intervals[i][0] <= end:
        start = start if start < intervals[i][0] else intervals[i][0]
        end = end if end > intervals[i][1] else intervals[i][1]
        i += 1
    result.append([start, end])

    while i < n:
        result.append(intervals[i])
        i += 1

    return result
