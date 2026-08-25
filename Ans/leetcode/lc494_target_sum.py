def find_target_sum_ways(nums: list[int], target: int) -> int:
    total = 0
    for n in nums:
        total += n
    if target > total or target < -total:
        return 0

    # 到達しうる和の範囲は [-total, total]。totalだけずらして0以上のインデックスにする
    size = 2 * total + 1
    dp = [0] * size
    dp[total] = 1  # 和0はインデックスtotal

    for n in nums:
        new_dp = [0] * size
        for s in range(size):
            if dp[s] == 0:
                continue
            if s + n < size:
                new_dp[s + n] += dp[s]
            if s - n >= 0:
                new_dp[s - n] += dp[s]
        dp = new_dp

    idx = target + total
    if idx < 0 or idx >= size:
        return 0
    return dp[idx]
