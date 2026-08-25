def cryptic_sorter(strings: list[str]) -> list[str]:
    # TODO: sorted()/.sort()を使わずに実装する
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check("basic", cryptic_sorter(["apple", "cat", "banana", "dog", "elephant"]),
          ["cat", "dog", "apple", "banana", "elephant"])
    check("case tie-break", cryptic_sorter(["aaa", "bbb", "AAA", "BBB"]),
          ["AAA", "aaa", "BBB", "bbb"])
    check("length then lex", cryptic_sorter(["hello", "world", "hi", "test"]),
          ["hi", "test", "hello", "world"])
    check("empty list", cryptic_sorter([]), [])
    check("single empty string", cryptic_sorter([""]), [""])
