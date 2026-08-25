class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None  # このノードで単語が完成する場合、その単語文字列を持つ


def find_words(board: list[list[str]], words: list[str]) -> list[str]:
    root = TrieNode()
    for w in words:
        node = root
        for ch in w:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.word = w

    rows, cols = len(board), len(board[0])
    result = []

    def dfs(r, c, node):
        ch = board[r][c]
        if ch not in node.children:
            return
        next_node = node.children[ch]
        if next_node.word:
            result.append(next_node.word)
            next_node.word = None  # 同じ単語を二重に追加しない

        board[r][c] = "#"
        if r > 0:
            dfs(r - 1, c, next_node)
        if r + 1 < rows:
            dfs(r + 1, c, next_node)
        if c > 0:
            dfs(r, c - 1, next_node)
        if c + 1 < cols:
            dfs(r, c + 1, next_node)
        board[r][c] = ch

    for r in range(rows):
        for c in range(cols):
            dfs(r, c, root)

    return result
