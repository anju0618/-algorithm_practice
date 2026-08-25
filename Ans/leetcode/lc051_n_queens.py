def solve_n_queens(n: int) -> list[list[str]]:
    result = []
    cols = [False] * n
    diag1 = [False] * (2 * n)  # r + c が同じマスは右上がり斜め上で一直線
    diag2 = [False] * (2 * n)  # r - c + n が同じマスは右下がり斜め上で一直線
    positions = [-1] * n       # positions[row] = そのrowでのcolumn

    def backtrack(row):
        if row == n:
            board = []
            for r in range(n):
                line = []
                for c in range(n):
                    line.append("Q" if positions[r] == c else ".")
                board.append("".join(line))
            result.append(board)
            return

        for c in range(n):
            if cols[c] or diag1[row + c] or diag2[row - c + n]:
                continue
            cols[c] = diag1[row + c] = diag2[row - c + n] = True
            positions[row] = c

            backtrack(row + 1)

            cols[c] = diag1[row + c] = diag2[row - c + n] = False
            positions[row] = -1

    backtrack(0)
    return result
