class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(root) -> str:
    result = []

    def dfs(node):
        if not node:
            result.append("N")
            return
        result.append(str(node.val))
        dfs(node.left)
        dfs(node.right)

    dfs(root)
    return ",".join(result)


def deserialize(data: str):
    values = data.split(",")
    index = [0]

    def build():
        val = values[index[0]]
        index[0] += 1
        if val == "N":
            return None
        node = TreeNode(int(val))
        node.left = build()
        node.right = build()
        return node

    return build()
