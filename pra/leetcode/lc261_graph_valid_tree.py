def valid_tree(n: int, edges: list[list[int]]) -> bool:
    # TODO: implement (Union-Find: n-1 edges and no cycle)
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check("valid tree", valid_tree(5, [[0, 1], [0, 2], [0, 3], [1, 4]]), True)
    check("has a cycle", valid_tree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]), False)
