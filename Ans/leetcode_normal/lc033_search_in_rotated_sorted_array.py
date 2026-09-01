def search_rotated(nums: list[int], target: int) -> int:
    for i, val in enumerate(nums):
        if val == target:
            return i
    return -1
