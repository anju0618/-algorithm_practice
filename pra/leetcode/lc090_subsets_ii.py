def subsets_with_dup(nums: list[int]) -> list[list[int]]:
    # TODO: implement (sort first without sorted(), skip same-depth duplicates)
    pass


def normalize(subsets_list):
    return sorted(tuple(s) for s in subsets_list)


def check(label, actual, expected):
    ok = normalize(actual) == normalize(expected)
    status = "[OK]" if ok else "[NG]"
    print(f"{status} {label}")
    if not ok:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check("with duplicate", subsets_with_dup([1, 2, 2]), [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]])
    check("single element", subsets_with_dup([0]), [[], [0]])
