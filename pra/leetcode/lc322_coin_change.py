def coin_change(coins: list[int], amount: int) -> int:
    # TODO: implement (bottom-up DP over amounts 0..amount)
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check("basic", coin_change([1, 2, 5], 11), 3)
    check("impossible", coin_change([2], 3), -1)
    check("zero amount", coin_change([1], 0), 0)
