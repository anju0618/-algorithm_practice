def max_product(nums: list[int]) -> int:
    best = nums[0]
    for i in range(len(nums)):
        product = 1
        for j in range(i, len(nums)):
            product *= nums[j]
            if product > best:
                best = product
    return best
