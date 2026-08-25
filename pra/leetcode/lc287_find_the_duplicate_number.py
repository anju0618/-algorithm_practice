def find_duplicate(nums: list[int]) -> int:
    # TODO: implement (Floyd's cycle detection over the array as an implicit linked list)
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check("basic", find_duplicate([1, 3, 4, 2, 2]), 2)
    check("duplicate not at end", find_duplicate([3, 1, 3, 4, 2]), 3)
    check("all same value", find_duplicate([3, 3, 3, 3, 3]), 3)
