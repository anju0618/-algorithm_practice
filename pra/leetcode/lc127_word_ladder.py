def ladder_length(begin_word: str, end_word: str, word_list: list[str]) -> int:
    # TODO: implement (BFS, trying every single-letter change at each step)
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check("path exists", ladder_length("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]), 5)
    check("end word not reachable", ladder_length("hit", "cog", ["hot", "dot", "dog", "lot", "log"]), 0)
