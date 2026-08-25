def can_partition(nums: list[int]) -> bool:
    total = 0
    for n in nums:
        total += n
    if total % 2 != 0:
        return False
    target = total // 2

    dp = [False] * (target + 1)
    dp[0] = True

    for n in nums:
        for s in range(target, n - 1, -1):  # 同じ数を2回使わないよう右から左に更新
            if dp[s - n]:
                dp[s] = True

    return dp[target]
