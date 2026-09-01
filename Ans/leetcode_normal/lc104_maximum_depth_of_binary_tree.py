class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_depth(root) -> int:
    if not root:
        return 0
    left = max_depth(root.left)
    right = max_depth(root.right)
    return 1 + (left if left > right else right)
