def contains_duplicate(nums: list[int]) -> bool:
    # TODO: implement without set()
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check("has duplicate", contains_duplicate([1, 2, 3, 1]), True)
    check("all distinct", contains_duplicate([1, 2, 3, 4]), False)
    check("multiple duplicates", contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]), True)
