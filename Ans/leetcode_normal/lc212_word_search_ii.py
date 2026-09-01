def find_words(board: list[list[str]], words: list[str]) -> list[str]:
    root = {}
    for w in words:
        node = root
        for ch in w:
            if ch not in node:
                node[ch] = {}
            node = node[ch]
        node["#"] = w

    rows, cols = len(board), len(board[0])
    result = []

    def dfs(r, c, node):
        ch = board[r][c]
        if ch not in node:
            return
        next_node = node[ch]
        if "#" in next_node:
            result.append(next_node["#"])
            del next_node["#"]  # 同じ単語を二重に追加しない

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
