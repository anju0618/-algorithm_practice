def merge_two_sorted_lists(list1: list[int], list2: list[int]) -> list[int]:
    # TODO: implement (two-pointer merge)
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check("basic", merge_two_sorted_lists([1, 2, 4], [1, 3, 4]), [1, 1, 2, 3, 4, 4])
    check("both empty", merge_two_sorted_lists([], []), [])
    check("one empty", merge_two_sorted_lists([], [0]), [0])
