def subsets(nums: list[int]) -> list[list[int]]:
    # TODO: implement (backtracking, include/exclude each element)
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
    check("basic", subsets([1, 2, 3]), [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]])
    check("single element", subsets([0]), [[], [0]])
