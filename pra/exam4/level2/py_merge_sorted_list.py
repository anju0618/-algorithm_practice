def merge_sorted_list(lists: list[list[int]]) -> list[int]:
    # TODO: implement without sorted()/.sort()/heapq
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check("three lists", merge_sorted_list([[1, 4, 5], [1, 3, 4], [2, 6]]), [1, 1, 2, 3, 4, 4, 5, 6])
    check("with empty sublist", merge_sorted_list([[1, 2, 3], [], [0, 4]]), [0, 1, 2, 3, 4])
    check("empty outer list", merge_sorted_list([]), [])
    check("all sublists empty", merge_sorted_list([[], []]), [])
