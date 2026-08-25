def two_sum_sorted(numbers: list[int], target: int) -> list[int]:
    # TODO: implement with two pointers, O(1) extra space
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check("basic", two_sum_sorted([2, 7, 11, 15], 9), [1, 2])
    check("skip a middle value", two_sum_sorted([2, 3, 4], 6), [1, 3])
    check("negative numbers", two_sum_sorted([-1, 0], -1), [1, 2])
