def swim_in_water(grid: list[list[int]]) -> int:
    n = len(grid)
    directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

    def can_reach(t):
        if grid[0][0] > t:
            return False
        visited = [[False] * n for _ in range(n)]
        visited[0][0] = True
        queue = [(0, 0)]
        while queue:
            next_queue = []
            for r, c in queue:
                if r == n - 1 and c == n - 1:
                    return True
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc] and grid[nr][nc] <= t:
                        visited[nr][nc] = True
                        next_queue.append((nr, nc))
            queue = next_queue
        return visited[n - 1][n - 1]

    max_height = 0
    for row in grid:
        for h in row:
            if h > max_height:
                max_height = h

    # 二分探索: 水位tでスタートからゴールに到達できる最小のtを探す
    left, right = 0, max_height
    while left < right:
        mid = (left + right) // 2
        if can_reach(mid):
            right = mid
        else:
            left = mid + 1
    return left
