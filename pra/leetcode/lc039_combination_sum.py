def combination_sum(candidates: list[int], target: int) -> list[list[int]]:
    # TODO: implement (backtracking, allow reusing the same index)
    pass


def normalize(combos):
    return sorted(tuple(sorted(c)) for c in combos)


def check(label, actual, expected):
    ok = normalize(actual) == normalize(expected)
    status = "[OK]" if ok else "[NG]"
    print(f"{status} {label}")
    if not ok:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check("basic", combination_sum([2, 3, 6, 7], 7), [[2, 2, 3], [7]])
    check("multiple combos", combination_sum([2, 3, 5], 8), [[2, 2, 2, 2], [2, 3, 3], [3, 5]])
