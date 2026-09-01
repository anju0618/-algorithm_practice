def can_partition(nums: list[int]) -> bool:
    total = 0
    for n in nums:
        total += n
    if total % 2 != 0:
        return False
    target = total // 2
    n = len(nums)

    # dp[i][s] = 最初のi個のnumsの中から選んで合計sを作れるか
    dp = [[False] * (target + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = True

    for i in range(1, n + 1):
        value = nums[i - 1]
        for s in range(target + 1):
            dp[i][s] = dp[i - 1][s]
            if s >= value and dp[i - 1][s - value]:
                dp[i][s] = True

    return dp[n][target]
