def missing_number(nums: list[int]) -> int:
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    actual_sum = 0
    for x in nums:
        actual_sum += x
    return expected_sum - actual_sum
