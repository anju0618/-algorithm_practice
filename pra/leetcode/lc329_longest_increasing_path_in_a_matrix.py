def longest_increasing_path(matrix: list[list[int]]) -> int:
    # TODO: implement (DFS + memoization from every cell)
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check("basic", longest_increasing_path([[9, 9, 4], [6, 6, 8], [2, 1, 1]]), 4)
    check("single cell", longest_increasing_path([[1]]), 1)
