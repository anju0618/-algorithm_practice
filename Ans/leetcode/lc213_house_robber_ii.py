def rob2(nums: list[int]) -> int:
    if len(nums) == 1:
        return nums[0]

    def rob_line(houses):
        prev2, prev1 = 0, 0
        for n in houses:
            take = prev2 + n
            current = prev1 if prev1 > take else take
            prev2, prev1 = prev1, current
        return prev1

    # 円形なので「最初の家を含めて最後を除く」か「最初を除いて最後を含める」の2択
    option1 = rob_line(nums[:-1])
    option2 = rob_line(nums[1:])
    return option1 if option1 > option2 else option2
