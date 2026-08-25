def max_profit_cooldown(prices: list[int]) -> int:
    # TODO: implement (state machine DP: hold / sold-today / resting)
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check("basic", max_profit_cooldown([1, 2, 3, 0, 2]), 3)
    check("single day", max_profit_cooldown([1]), 0)
