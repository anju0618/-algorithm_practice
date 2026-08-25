class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class WordDictionary:
    def __init__(self):
        # TODO: implement (trie, with DFS in search() to handle '.')
        pass

    def add_word(self, word: str) -> None:
        pass

    def search(self, word: str) -> bool:
        pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    wd = WordDictionary()
    wd.add_word("bad")
    wd.add_word("dad")
    wd.add_word("mad")
    check("no match", wd.search("pad"), False)
    check("exact match", wd.search("bad"), True)
    check("wildcard first char", wd.search(".ad"), True)
    check("wildcard last two chars", wd.search("b.."), True)
