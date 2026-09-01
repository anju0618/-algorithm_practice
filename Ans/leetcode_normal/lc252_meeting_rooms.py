def can_attend_meetings(intervals: list[list[int]]) -> bool:
    n = len(intervals)
    for i in range(n):
        a_start, a_end = intervals[i]
        for j in range(i + 1, n):
            b_start, b_end = intervals[j]
            if a_start < b_end and b_start < a_end:
                return False
    return True
