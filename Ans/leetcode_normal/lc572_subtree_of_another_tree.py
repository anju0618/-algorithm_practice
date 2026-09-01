class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_subtree(root, sub_root) -> bool:
    def same(a, b):
        if not a and not b:
            return True
        if not a or not b:
            return False
        return a.val == b.val and same(a.left, b.left) and same(a.right, b.right)

    if not root:
        return sub_root is None
    if same(root, sub_root):
        return True
    return is_subtree(root.left, sub_root) or is_subtree(root.right, sub_root)
