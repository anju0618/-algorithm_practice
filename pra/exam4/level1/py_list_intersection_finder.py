def list_intersection_finder(lists: list[list[int]]) -> list[int]:
    # TODO: implement without sorted()/set()
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check("basic", list_intersection_finder([[1, 2, 3], [2, 3, 4], [2, 3, 5]]), [2, 3])
    check("single common element", list_intersection_finder([[1, 2, 3, 4], [2, 4, 6, 8], [4, 8, 12]]), [4])
    check("with duplicates in input", list_intersection_finder([[1, 1, 2, 3], [1, 2, 2, 3], [1, 2, 3, 3]]), [1, 2, 3])
    check("no overlap", list_intersection_finder([[1, 2, 3], [4, 5, 6]]), [])
    check("no lists", list_intersection_finder([]), [])
    check("one list empty", list_intersection_finder([[1, 2, 3], []]), [])
    check("single list", list_intersection_finder([[5]]), [5])
