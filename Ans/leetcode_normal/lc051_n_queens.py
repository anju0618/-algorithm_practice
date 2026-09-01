def solve_n_queens(n: int) -> list[list[str]]:
    result = []
    positions = [-1] * n  # positions[row] = そのrowでのcolumn

    def is_valid(row, col):
        for r in range(row):
            c = positions[r]
            if c == col:
                return False
            if abs(r - row) == abs(c - col):
                return False
        return True

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
            if is_valid(row, c):
                positions[row] = c
                backtrack(row + 1)
                positions[row] = -1

    backtrack(0)
    return result
