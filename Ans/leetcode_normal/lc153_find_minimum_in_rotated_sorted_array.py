def find_min(nums: list[int]) -> int:
    min_val = nums[0]
    for n in nums:
        if n < min_val:
            min_val = n
    return min_val
