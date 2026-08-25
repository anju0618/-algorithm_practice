def min_window(s: str, t: str) -> str:
    # TODO: implement (variable sliding window with need/window counts)
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check("basic", min_window("ADOBECODEBANC", "ABC"), "BANC")
    check("whole string is the window", min_window("a", "a"), "a")
    check("not enough characters", min_window("a", "aa"), "")
