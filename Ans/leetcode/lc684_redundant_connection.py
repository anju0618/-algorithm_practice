def find_redundant_connection(edges: list[list[int]]) -> list[int]:
    n = len(edges)
    parent = list(range(n + 1))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]  # 経路の半分を圧縮（path halving）
            x = parent[x]
        return x

    for a, b in edges:
        root_a, root_b = find(a), find(b)
        if root_a == root_b:
            return [a, b]  # すでに繋がっている2頂点をまた繋ぐ辺 = 余分な辺
        parent[root_a] = root_b
    return []
