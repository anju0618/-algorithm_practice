def combination_sum2(candidates: list[int], target: int) -> list[list[int]]:
    # TODO: implement (sort first without sorted(), backtrack, skip same-depth duplicates)
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
    check("basic", combination_sum2([10, 1, 2, 7, 6, 1, 5], 8), [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]])
    check("with many duplicates", combination_sum2([2, 5, 2, 1, 2], 5), [[1, 2, 2], [5]])
