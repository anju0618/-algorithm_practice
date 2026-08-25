def rotate(matrix: list[list[int]]) -> None:
    # TODO: implement (transpose in place, then reverse each row)
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    rotate(m)
    check("basic", m, [[7, 4, 1], [8, 5, 2], [9, 6, 3]])
