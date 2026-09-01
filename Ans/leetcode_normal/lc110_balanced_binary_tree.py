class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def height(node) -> int:
    if not node:
        return 0
    left_h = height(node.left)
    right_h = height(node.right)
    return 1 + (left_h if left_h > right_h else right_h)


def is_balanced(root) -> bool:
    if not root:
        return True

    left_h = height(root.left)
    right_h = height(root.right)
    diff = left_h - right_h if left_h > right_h else right_h - left_h

    if diff > 1:
        return False
    return is_balanced(root.left) and is_balanced(root.right)
