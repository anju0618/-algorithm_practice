def permute(nums: list[int]) -> list[list[int]]:
    # TODO: implement (backtracking with a used[] marker)
    pass


def normalize(perms):
    return sorted(tuple(p) for p in perms)


def check(label, actual, expected):
    ok = normalize(actual) == normalize(expected)
    status = "[OK]" if ok else "[NG]"
    print(f"{status} {label}")
    if not ok:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check("basic", permute([1, 2, 3]), [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]])
    check("two elements", permute([0, 1]), [[0, 1], [1, 0]])
