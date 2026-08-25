class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def diameter_of_binary_tree(root) -> int:
    best = [0]  # クロージャから書き換えるためリストに包む

    def height(node):
        if not node:
            return 0
        left = height(node.left)
        right = height(node.right)
        if left + right > best[0]:
            best[0] = left + right
        return 1 + (left if left > right else right)

    height(root)
    return best[0]
