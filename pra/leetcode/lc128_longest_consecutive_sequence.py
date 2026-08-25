def longest_consecutive(nums: list[int]) -> int:
    # TODO: implement in O(n) without set()
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check("basic", longest_consecutive([100, 4, 200, 1, 3, 2]), 4)
    check("longer run", longest_consecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]), 9)
    check("with duplicate", longest_consecutive([1, 0, 1, 2]), 3)
