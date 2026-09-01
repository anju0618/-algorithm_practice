def rotate_array(nums: list[int], k: int) -> list[int]:
    if not nums:
        return []
    n = len(nums)
    real_k = k % n
    if real_k == 0:
        return nums[:]

    result = []
    for i in range(n - real_k, n):
        result.append(nums[i])
    for i in range(0, n - real_k):
        result.append(nums[i])
    return result
