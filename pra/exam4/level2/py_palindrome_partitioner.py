def palindrome_partitioner(s: str) -> int:
    # TODO: implement (DP)
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check("one cut needed", palindrome_partitioner("aab"), 1)
    check("already palindrome", palindrome_partitioner("aba"), 0)
    check("all distinct", palindrome_partitioner("abc"), 2)
