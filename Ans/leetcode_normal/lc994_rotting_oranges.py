def oranges_rotting(grid: list[list[int]]) -> int:
    rows, cols = len(grid), len(grid[0])
    queue = []
    fresh = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                queue.append((r, c))
            elif grid[r][c] == 1:
                fresh += 1

    minutes = 0
    directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

    while queue and fresh > 0:
        next_queue = []
        for r, c in queue:
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh -= 1
                    next_queue.append((nr, nc))
        if next_queue:
            minutes += 1
        queue = next_queue

    return minutes if fresh == 0 else -1
