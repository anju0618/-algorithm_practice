def max_coins(nums: list[int]) -> int:
    # TODO: implement (interval DP: think about which balloon bursts LAST in each range)
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check("basic", max_coins([3, 1, 5, 8]), 167)
    check("two balloons", max_coins([1, 5]), 10)
