def search_matrix(matrix: list[list[int]], target: int) -> bool:
    # TODO: implement (treat as a flattened sorted array)
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    check("target present", search_matrix(matrix, 3), True)
    check("target absent", search_matrix(matrix, 13), False)
