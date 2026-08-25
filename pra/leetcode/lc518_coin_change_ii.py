def change(amount: int, coins: list[int]) -> int:
    # TODO: implement (unbounded knapsack counting combinations, coin as the outer loop)
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check("basic", change(5, [1, 2, 5]), 4)
    check("impossible", change(3, [2]), 0)
    check("exact single coin", change(10, [10]), 1)
