class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_balanced(root) -> bool:
    def check(node):
        if not node:
            return 0, True
        left_h, left_ok = check(node.left)
        right_h, right_ok = check(node.right)
        diff = left_h - right_h if left_h > right_h else right_h - left_h
        ok = left_ok and right_ok and diff <= 1
        height = 1 + (left_h if left_h > right_h else right_h)
        return height, ok

    return check(root)[1]
