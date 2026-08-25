def rob2(nums: list[int]) -> int:
    # TODO: implement (run linear House Robber twice, excluding first or last house)
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check("three houses", rob2([2, 3, 2]), 3)
    check("four houses", rob2([1, 2, 3, 1]), 4)
    check("adjacent wrap", rob2([1, 2, 3]), 3)
