def set_zeroes(matrix: list[list[int]]) -> None:
    # TODO: implement (use the first row/column as markers, O(1) extra space)
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    m1 = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    set_zeroes(m1)
    check("basic", m1, [[1, 0, 1], [0, 0, 0], [1, 0, 1]])

    m2 = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    set_zeroes(m2)
    check("zero on border", m2, [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]])
