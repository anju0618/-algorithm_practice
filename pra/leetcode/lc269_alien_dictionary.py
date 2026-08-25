def alien_order(words: list[str]) -> str:
    # TODO: implement (build a letter-order graph from adjacent word pairs, then topological sort)
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check("basic", alien_order(["wrt", "wrf", "er", "ett", "rftt"]), "wertf")
    check("two letters", alien_order(["z", "x"]), "zx")
    check("cycle", alien_order(["z", "x", "z"]), "")
