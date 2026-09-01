def contains_duplicate(nums: list[int]) -> bool:
    seen = {}
    for n in nums:
        if n in seen:
            return True
        seen[n] = True
    return False
