def max_profit(prices: list[int]) -> int:
    # TODO: implement (single pass, track running minimum)
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check("basic", max_profit([7, 1, 5, 3, 6, 4]), 5)
    check("no profit possible", max_profit([7, 6, 4, 3, 1]), 0)
