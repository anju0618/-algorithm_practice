def search_rotated(nums: list[int], target: int) -> int:
    # TODO: implement (modified binary search)
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check("target in right half", search_rotated([4, 5, 6, 7, 0, 1, 2], 0), 4)
    check("target absent", search_rotated([4, 5, 6, 7, 0, 1, 2], 3), -1)
    check("single element, not found", search_rotated([1], 0), -1)
