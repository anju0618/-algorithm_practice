def min_cost_climbing_stairs(cost: list[int]) -> int:
    # TODO: implement (DP, dp[i] = min cost to reach step i)
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check("basic", min_cost_climbing_stairs([10, 15, 20]), 15)
    check("longer array", min_cost_climbing_stairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]), 6)
