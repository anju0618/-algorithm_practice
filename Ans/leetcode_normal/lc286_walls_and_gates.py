INF = 2147483647


def walls_and_gates(rooms: list[list[int]]) -> None:
    if not rooms:
        return
    rows, cols = len(rooms), len(rooms[0])

    queue = []
    for r in range(rows):
        for c in range(cols):
            if rooms[r][c] == 0:
                queue.append((r, c))

    directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
    head = 0
    while head < len(queue):
        r, c = queue[head]
        head += 1
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and rooms[nr][nc] == INF:
                rooms[nr][nc] = rooms[r][c] + 1
                queue.append((nr, nc))
