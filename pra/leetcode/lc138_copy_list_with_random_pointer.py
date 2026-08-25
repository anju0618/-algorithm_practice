class Node:
    def __init__(self, val, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random


def copy_random_list(head):
    # TODO: implement (old-node -> new-node dict, two passes)
    pass


def build(vals, random_idx):
    nodes = [Node(v) for v in vals]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    for i, r in enumerate(random_idx):
        if r is not None:
            nodes[i].random = nodes[r]
    return nodes[0] if nodes else None


def to_pairs(head):
    result = []
    nodes = []
    curr = head
    while curr:
        nodes.append(curr)
        curr = curr.next
    index = {node: i for i, node in enumerate(nodes)}
    for node in nodes:
        r = index[node.random] if node.random else None
        result.append((node.val, r))
    return result


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    original = build([7, 13, 11], [None, 0, None])
    copy = copy_random_list(original)
    check("structure matches", to_pairs(copy), to_pairs(original))
    check("nodes are new objects", copy is not original, True)
