def rob(nums: list[int]) -> int:
    # TODO: implement (DP: skip this house vs. rob it + best up to two houses back)
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check("basic", rob([1, 2, 3, 1]), 4)
    check("longer array", rob([2, 7, 9, 3, 1]), 12)
