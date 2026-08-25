class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def lowest_common_ancestor(root, p, q):
    # TODO: implement (use BST ordering to steer left/right, no recursion needed)
    pass


def build_bst(values):
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while queue and i < len(values):
        node = queue.pop(0)
        if i < len(values):
            if values[i] is not None:
                node.left = TreeNode(values[i])
                queue.append(node.left)
            i += 1
        if i < len(values):
            if values[i] is not None:
                node.right = TreeNode(values[i])
                queue.append(node.right)
            i += 1
    return root


def find_node(root, val):
    node = root
    while node and node.val != val:
        node = node.left if val < node.val else node.right
    return node


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    root = build_bst([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
    check("split across branches", lowest_common_ancestor(root, find_node(root, 2), find_node(root, 8)).val, 6)
    check("ancestor is p itself", lowest_common_ancestor(root, find_node(root, 2), find_node(root, 4)).val, 2)
