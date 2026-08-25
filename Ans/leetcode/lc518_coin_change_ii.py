def change(amount: int, coins: list[int]) -> int:
    dp = [0] * (amount + 1)
    dp[0] = 1

    # コインを外側のループにすることで「組み合わせ」を数える（順列と重複しない）
    for c in coins:
        for a in range(c, amount + 1):
            dp[a] += dp[a - c]

    return dp[amount]
