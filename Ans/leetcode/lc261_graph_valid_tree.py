def valid_tree(n: int, edges: list[list[int]]) -> bool:
    # 木であるための必要条件: 辺の数がちょうどn-1
    if len(edges) != n - 1:
        return False

    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for a, b in edges:
        root_a, root_b = find(a), find(b)
        if root_a == root_b:
            return False  # すでに繋がっている2頂点をまた繋ぐ = サイクルができる
        parent[root_a] = root_b

    return True
