def max_sub_array(nums: list[int]) -> int:
    best = nums[0]
    current = nums[0]
    for n in nums[1:]:
        extended = current + n
        current = n if n > extended else extended
        if current > best:
            best = current
    return best
