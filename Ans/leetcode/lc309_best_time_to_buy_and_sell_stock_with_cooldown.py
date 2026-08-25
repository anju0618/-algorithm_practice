def max_profit_cooldown(prices: list[int]) -> int:
    if not prices:
        return 0

    hold = -prices[0]  # 株を持っている状態での最大利益
    sold = 0            # 今日売った状態での最大利益
    rest = 0             # 株を持たず、クールダウンでもない状態での最大利益

    for p in prices[1:]:
        prev_sold = sold
        sold = hold + p
        new_hold = rest - p if rest - p > hold else hold
        new_rest = prev_sold if prev_sold > rest else rest
        hold = new_hold
        rest = new_rest

    return sold if sold > rest else rest
