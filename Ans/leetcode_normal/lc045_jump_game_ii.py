def jump(nums: list[int]) -> int:
    n = len(nums)
    dp = [float("inf")] * n
    dp[0] = 0

    for i in range(n):
        if dp[i] == float("inf"):
            continue
        farthest = i + nums[i]
        if farthest > n - 1:
            farthest = n - 1
        for j in range(i + 1, farthest + 1):
            if dp[i] + 1 < dp[j]:
                dp[j] = dp[i] + 1

    return dp[n - 1]
