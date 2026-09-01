class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_path_sum(root) -> int:
    best = root.val

    def max_gain(node):
        nonlocal best
        if not node:
            return 0

        left_gain = max_gain(node.left)
        if left_gain < 0:
            left_gain = 0
        right_gain = max_gain(node.right)
        if right_gain < 0:
            right_gain = 0

        # このノードを頂点として左右両方を使うパスの合計（戻り値ではなく記録用）
        path_sum = node.val + left_gain + right_gain
        if path_sum > best:
            best = path_sum

        # 親に返せるのは片側だけを使った「腕」の長さ
        return node.val + (left_gain if left_gain > right_gain else right_gain)

    max_gain(root)
    return best
