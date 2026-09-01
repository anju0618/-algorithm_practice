def num_distinct(s: str, t: str) -> int:
    m, n = len(s), len(t)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = 1  # 空文字列tを作る方法は常に1通り（何も選ばない）

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            dp[i][j] = dp[i - 1][j]  # s[i-1]を使わない場合
            if s[i - 1] == t[j - 1]:
                dp[i][j] += dp[i - 1][j - 1]  # s[i-1]を使う場合

    return dp[m][n]
