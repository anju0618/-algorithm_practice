class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self):
        # TODO: implement
        pass

    def insert(self, word: str) -> None:
        pass

    def search(self, word: str) -> bool:
        pass

    def starts_with(self, prefix: str) -> bool:
        pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    trie = Trie()
    trie.insert("apple")
    check("exact match", trie.search("apple"), True)
    check("no exact match yet", trie.search("app"), False)
    check("prefix match", trie.starts_with("app"), True)
    trie.insert("app")
    check("exact match after insert", trie.search("app"), True)
