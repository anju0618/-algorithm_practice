def mirror_matrix(matrix: list[list[int]]) -> list[list[int]]:
    result = []
    for row in matrix:
        reversed_row = []
        for i in range(len(row) - 1, -1, -1):
            reversed_row.append(row[i])
        result.append(reversed_row)
    return result
