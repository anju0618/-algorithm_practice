def mirror_matrix(matrix: list[list[int]]) -> list[list[int]]:
    # TODO: 実装する
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check("2x3", mirror_matrix([[1, 2, 3], [4, 5, 6]]), [[3, 2, 1], [6, 5, 4]])
    check("3x2", mirror_matrix([[1, 2], [3, 4], [5, 6]]), [[2, 1], [4, 3], [6, 5]])
    check("1x1", mirror_matrix([[7]]), [[7]])
    check("1x4", mirror_matrix([[1, 2, 3, 4]]), [[4, 3, 2, 1]])
    check("negatives", mirror_matrix([[-1, -2], [-3, -4]]), [[-2, -1], [-4, -3]])
