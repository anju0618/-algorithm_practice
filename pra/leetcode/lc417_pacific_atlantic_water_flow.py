def pacific_atlantic(heights: list[list[int]]) -> list[list[int]]:
    # TODO: implement (DFS inward from each ocean's border, intersect the reachable sets)
    pass


def check(label, actual, expected):
    ok = sorted(map(tuple, actual)) == sorted(map(tuple, expected))
    status = "[OK]" if ok else "[NG]"
    print(f"{status} {label}")
    if not ok:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check("basic", pacific_atlantic([[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]),
          [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]])
    check("single cell", pacific_atlantic([[1]]), [[0, 0]])
