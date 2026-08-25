def group_anagrams(strs: list[str]) -> list[list[str]]:
    # TODO: implement without sorted()
    pass


def normalize(groups):
    # テスト比較専用のヘルパー。順序を問わない出力を比較するためだけに使う
    # （Ans側の実装でsorted()を使うわけではない）
    return sorted(sorted(g) for g in groups)


def check(label, actual, expected):
    status = "[OK]" if normalize(actual) == normalize(expected) else "[NG]"
    print(f"{status} {label}")
    if normalize(actual) != normalize(expected):
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check("basic", group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]),
          [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]])
    check("single empty string", group_anagrams([""]), [[""]])
    check("single char", group_anagrams(["a"]), [["a"]])
