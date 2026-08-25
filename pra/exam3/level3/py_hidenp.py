def hidenp(small: str, big: str) -> bool:
    # TODO: implement
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check("interleaved digits", hidenp("abc", "a1b2c3"), True)
    check("valid subsequence", hidenp("ace", "abcde"), True)
    check("wrong order", hidenp("aec", "abcde"), False)
    check("empty small", hidenp("", "abc"), True)
    check("small longer than big", hidenp("abc", "ab"), False)
    check("not enough repeats", hidenp("aaaa", "aaa"), False)
    check("word in sentence", hidenp("sing", "subsequence testing"), True)
