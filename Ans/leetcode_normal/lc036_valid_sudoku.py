def is_valid_sudoku(board: list[list[str]]) -> bool:
    rows = [{} for _ in range(9)]
    cols = [{} for _ in range(9)]
    boxes = [{} for _ in range(9)]

    for r in range(9):
        for c in range(9):
            val = board[r][c]
            if val == ".":
                continue
            b = (r // 3) * 3 + (c // 3)
            if val in rows[r] or val in cols[c] or val in boxes[b]:
                return False
            rows[r][val] = True
            cols[c][val] = True
            boxes[b][val] = True
    return True
