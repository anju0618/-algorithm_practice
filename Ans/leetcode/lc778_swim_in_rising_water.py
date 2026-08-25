def swim_in_water(grid: list[list[int]]) -> int:
    n = len(grid)
    visited = [[False] * n for _ in range(n)]
    heap = [(grid[0][0], 0, 0)]  # (そのマスに到達するのに必要な最小の水位, r, c)

    def push(item):
        heap.append(item)
        i = len(heap) - 1
        while i > 0:
            parent = (i - 1) // 2
            if heap[parent][0] <= heap[i][0]:
                break
            heap[parent], heap[i] = heap[i], heap[parent]
            i = parent

    def pop():
        top = heap[0]
        last = heap.pop()
        if heap:
            heap[0] = last
            i, size = 0, len(heap)
            while True:
                left, right, smallest = 2 * i + 1, 2 * i + 2, i
                if left < size and heap[left][0] < heap[smallest][0]:
                    smallest = left
                if right < size and heap[right][0] < heap[smallest][0]:
                    smallest = right
                if smallest == i:
                    break
                heap[i], heap[smallest] = heap[smallest], heap[i]
                i = smallest
        return top

    visited[0][0] = True
    best = 0
    directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

    while heap:
        t, r, c = pop()
        if t > best:
            best = t
        if r == n - 1 and c == n - 1:
            return best
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                visited[nr][nc] = True
                push((grid[nr][nc], nr, nc))
    return best
