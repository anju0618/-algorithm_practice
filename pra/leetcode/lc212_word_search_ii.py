class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None


def find_words(board: list[list[str]], words: list[str]) -> list[str]:
    # TODO: implement (build a trie of all words, DFS the board once)
    pass


def check(label, actual, expected):
    ok = sorted(actual) == sorted(expected)
    status = "[OK]" if ok else "[NG]"
    print(f"{status} {label}")
    if not ok:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    board = [["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]]
    check("basic", find_words(board, ["oath", "pea", "eat", "rain"]), ["eat", "oath"])
    check("no matches", find_words([["a", "b"], ["c", "d"]], ["abcb"]), [])
