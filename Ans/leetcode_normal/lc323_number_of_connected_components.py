def count_components(n: int, edges: list[list[int]]) -> int:
    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            x = parent[x]
        return x

    for a, b in edges:
        root_a, root_b = find(a), find(b)
        if root_a != root_b:
            parent[root_a] = root_b

    roots = {}
    for i in range(n):
        roots[find(i)] = True
    return len(roots)
