def find_min(nums: list[int]) -> int:
    # TODO: implement (binary search against the right endpoint)
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check("basic", find_min([3, 4, 5, 1, 2]), 1)
    check("rotated near end", find_min([4, 5, 6, 7, 0, 1, 2]), 0)
    check("not rotated", find_min([11, 13, 15, 17]), 11)
