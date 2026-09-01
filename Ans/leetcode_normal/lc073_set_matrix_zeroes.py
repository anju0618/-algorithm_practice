def set_zeroes(matrix: list[list[int]]) -> None:
    rows, cols = len(matrix), len(matrix[0])
    zero_rows = []
    zero_cols = []

    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 0:
                if r not in zero_rows:
                    zero_rows.append(r)
                if c not in zero_cols:
                    zero_cols.append(c)

    for r in range(rows):
        for c in range(cols):
            if r in zero_rows or c in zero_cols:
                matrix[r][c] = 0
