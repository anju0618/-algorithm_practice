def single_number(nums: list[int]) -> int:
    counts = {}
    for n in nums:
        counts[n] = counts.get(n, 0) + 1

    for n, c in counts.items():
        if c == 1:
            return n
    return -1
