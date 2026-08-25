def max_product(nums: list[int]) -> int:
    result = nums[0]
    cur_max = nums[0]
    cur_min = nums[0]

    for n in nums[1:]:
        if n < 0:
            cur_max, cur_min = cur_min, cur_max  # 負の数を掛けると最大最小が入れ替わる

        cand_max = cur_max * n
        cur_max = n if n > cand_max else cand_max
        cand_min = cur_min * n
        cur_min = n if n < cand_min else cand_min

        if cur_max > result:
            result = cur_max

    return result
