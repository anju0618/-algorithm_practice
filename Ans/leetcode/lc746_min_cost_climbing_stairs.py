def min_cost_climbing_stairs(cost: list[int]) -> int:
    n = len(cost)
    prev2, prev1 = 0, 0
    for i in range(2, n + 1):
        option_a = prev1 + cost[i - 1]
        option_b = prev2 + cost[i - 2]
        current = option_a if option_a < option_b else option_b
        prev2, prev1 = prev1, current
    return prev1
