def max_profit_cooldown(prices: list[int]) -> int:
    if not prices:
        return 0

    n = len(prices)
    hold = [0] * n  # 株を持っている状態での最大利益
    sold = [0] * n  # 今日売った状態での最大利益
    rest = [0] * n  # 株を持たず、クールダウンでもない状態での最大利益

    hold[0] = -prices[0]

    for i in range(1, n):
        hold[i] = max(hold[i - 1], rest[i - 1] - prices[i])
        sold[i] = hold[i - 1] + prices[i]
        rest[i] = max(rest[i - 1], sold[i - 1])

    return max(sold[n - 1], rest[n - 1])
