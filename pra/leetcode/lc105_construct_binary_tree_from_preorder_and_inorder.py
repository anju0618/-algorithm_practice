class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(preorder, inorder):
    # TODO: implement (preorder[0] is the root, find it in inorder to split)
    pass


def tree_to_values(root):
    if not root:
        return []
    result = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    return result


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check("basic", tree_to_values(build_tree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])), [3, 9, 20, None, None, 15, 7])
    check("single node", tree_to_values(build_tree([-1], [-1])), [-1])
