def intersection(nums1: list[int], nums2: list[int]) -> list[int]:
    # TODO: implement without set()
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check("with duplicates", intersection([1, 2, 2, 1], [2, 2]), [2])
    check("basic", intersection([4, 9, 5], [9, 4, 9, 8, 4]), [4, 9])
