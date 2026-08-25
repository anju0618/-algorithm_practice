def length_of_longest_substring(s: str) -> int:
    # TODO: implement (sliding window with last-seen index)
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check("basic", length_of_longest_substring("abcabcbb"), 3)
    check("all same char", length_of_longest_substring("bbbbb"), 1)
    check("substring not subsequence", length_of_longest_substring("pwwkew"), 3)
