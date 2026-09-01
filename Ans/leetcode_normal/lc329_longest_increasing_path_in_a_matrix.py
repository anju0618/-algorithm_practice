def longest_increasing_path(matrix: list[list[int]]) -> int:
    rows, cols = len(matrix), len(matrix[0])
    memo = [[0] * cols for _ in range(rows)]

    def dfs(r, c):
        if memo[r][c]:
            return memo[r][c]
        best = 1
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] > matrix[r][c]:
                length = 1 + dfs(nr, nc)
                if length > best:
                    best = length
        memo[r][c] = best
        return best

    result = 0
    for r in range(rows):
        for c in range(cols):
            length = dfs(r, c)
            if length > result:
                result = length
    return result
