class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def good_nodes(root) -> int:
    if not root:
        return 0

    def dfs(node, max_so_far):
        if not node:
            return 0
        count = 1 if node.val >= max_so_far else 0
        new_max = node.val if node.val > max_so_far else max_so_far
        return count + dfs(node.left, new_max) + dfs(node.right, new_max)

    return dfs(root, root.val)
