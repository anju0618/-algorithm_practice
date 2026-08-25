def partition(s: str) -> list[list[str]]:
    # TODO: implement (backtracking, only extend with palindromic prefixes)
    pass


def normalize(partitions):
    return sorted(tuple(p) for p in partitions)


def check(label, actual, expected):
    ok = normalize(actual) == normalize(expected)
    status = "[OK]" if ok else "[NG]"
    print(f"{status} {label}")
    if not ok:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check("basic", partition("aab"), [["a", "a", "b"], ["aa", "b"]])
    check("single char", partition("a"), [["a"]])
