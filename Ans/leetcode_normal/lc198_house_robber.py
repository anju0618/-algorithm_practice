def rob(nums: list[int]) -> int:
    if not nums:
        return 0
    n = len(nums)
    dp = [0] * (n + 1)
    dp[1] = nums[0]
    for i in range(2, n + 1):
        take = dp[i - 2] + nums[i - 1]
        skip = dp[i - 1]
        dp[i] = take if take > skip else skip
    return dp[n]
