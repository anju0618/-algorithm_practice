class WordDictionary:
    def __init__(self):
        self.root = {}

    def add_word(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node:
                node[ch] = {}
            node = node[ch]
        node["#"] = True

    def search(self, word: str) -> bool:
        def dfs(node, i):
            if i == len(word):
                return "#" in node
            ch = word[i]
            if ch == ".":
                for key, child in node.items():
                    if key != "#" and dfs(child, i + 1):
                        return True
                return False
            if ch not in node:
                return False
            return dfs(node[ch], i + 1)

        return dfs(self.root, 0)
