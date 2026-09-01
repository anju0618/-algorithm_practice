def rob2(nums: list[int]) -> int:
    if len(nums) == 1:
        return nums[0]

    def rob_line(houses):
        n = len(houses)
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            take = dp[i - 2] + houses[i - 1] if i >= 2 else houses[i - 1]
            skip = dp[i - 1]
            dp[i] = take if take > skip else skip
        return dp[n]

    option1 = rob_line(nums[:-1])
    option2 = rob_line(nums[1:])
    return option1 if option1 > option2 else option2
