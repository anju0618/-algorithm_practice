def merge_k_sorted_lists(lists: list[list[int]]) -> list[int]:
    # TODO: implement (fold pairwise merges)
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check("three lists", merge_k_sorted_lists([[1, 4, 5], [1, 3, 4], [2, 6]]), [1, 1, 2, 3, 4, 4, 5, 6])
    check("empty outer list", merge_k_sorted_lists([]), [])
    check("single empty list", merge_k_sorted_lists([[]]), [])
