def intersection(nums1: list[int], nums2: list[int]) -> list[int]:
    result = []
    for value in nums1:
        if value in nums2 and value not in result:
            result.append(value)
    return result
