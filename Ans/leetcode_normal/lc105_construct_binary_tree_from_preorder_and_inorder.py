class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(preorder, inorder):
    if not preorder:
        return None

    root_val = preorder[0]
    root = TreeNode(root_val)

    mid = 0
    for i, v in enumerate(inorder):
        if v == root_val:
            mid = i
            break

    root.left = build_tree(preorder[1:mid + 1], inorder[:mid])
    root.right = build_tree(preorder[mid + 1:], inorder[mid + 1:])
    return root
