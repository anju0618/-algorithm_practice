def exist(board: list[list[str]], word: str) -> bool:
    # TODO: implement (DFS/backtracking with temporary in-place marking)
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    check("word exists", exist(board, "ABCCED"), True)
    check("word does not exist", exist(board, "ABCB"), False)
