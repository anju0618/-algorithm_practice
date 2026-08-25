def shadow_merge(list1: list[int], list2: list[int]) -> list[int]:
    # TODO: implement using a two-pointer merge, no sorted()
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check("interleaved", shadow_merge([1, 3, 5], [2, 4, 6]), [1, 2, 3, 4, 5, 6])
    check("already ordered blocks", shadow_merge([1, 2, 3], [4, 5, 6]), [1, 2, 3, 4, 5, 6])
    check("single element first", shadow_merge([1], [2, 3, 4]), [1, 2, 3, 4])
    check("empty first list", shadow_merge([], [1, 2, 3]), [1, 2, 3])
    check("with duplicates", shadow_merge([1, 1, 2], [1, 3, 3]), [1, 1, 1, 2, 3, 3])
