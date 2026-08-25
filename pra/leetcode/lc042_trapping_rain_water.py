def trap(height: list[int]) -> int:
    # TODO: implement with two pointers, O(1) extra space
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check("basic", trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]), 6)
    check("no flat start/end", trap([4, 2, 0, 3, 2, 5]), 9)
