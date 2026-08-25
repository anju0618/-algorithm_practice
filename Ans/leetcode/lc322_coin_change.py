def coin_change(coins: list[int], amount: int) -> int:
    infinity = amount + 1
    dp = [infinity] * (amount + 1)
    dp[0] = 0

    for a in range(1, amount + 1):
        for c in coins:
            if c <= a and dp[a - c] + 1 < dp[a]:
                dp[a] = dp[a - c] + 1

    return dp[amount] if dp[amount] != infinity else -1
