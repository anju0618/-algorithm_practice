def rob(nums: list[int]) -> int:
    prev2, prev1 = 0, 0
    for n in nums:
        take = prev2 + n
        current = prev1 if prev1 > take else take
        prev2, prev1 = prev1, current
    return prev1
