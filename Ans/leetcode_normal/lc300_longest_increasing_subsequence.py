def length_of_lis(nums: list[int]) -> int:
    n = len(nums)
    # dp[i] = nums[i]で終わる最長増加部分列の長さ
    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            if nums[j] < nums[i] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1

    best = 0
    for length in dp:
        if length > best:
            best = length
    return best
