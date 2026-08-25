class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def clone_graph(node):
    # TODO: implement (DFS with an old-node -> new-node dict to avoid infinite loops)
    pass


def build_graph(adj):
    # adj: {val: [neighbor_val, ...]}
    nodes = {val: Node(val) for val in adj}
    for val, neighbors in adj.items():
        for nv in neighbors:
            nodes[val].neighbors.append(nodes[nv])
    return nodes[1] if nodes else None


def to_adj(start):
    if not start:
        return {}
    visited = {}
    stack = [start]
    while stack:
        n = stack.pop()
        if n.val in visited:
            continue
        visited[n.val] = sorted(nb.val for nb in n.neighbors)
        for nb in n.neighbors:
            if nb.val not in visited:
                stack.append(nb)
    return visited


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    original = build_graph({1: [2, 4], 2: [1, 3], 3: [2, 4], 4: [1, 3]})
    copy = clone_graph(original)
    check("structure matches", to_adj(copy), to_adj(original))
    check("root is a new object", copy is not original, True)
