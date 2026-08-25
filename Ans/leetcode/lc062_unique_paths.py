def unique_paths(m: int, n: int) -> int:
    dp = [1] * n  # 1行分だけ保持する（O(n)空間）
    for _ in range(m - 1):
        for j in range(1, n):
            dp[j] += dp[j - 1]
    return dp[-1]
