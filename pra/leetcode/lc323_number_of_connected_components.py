def count_components(n: int, edges: list[list[int]]) -> int:
    # TODO: implement (Union-Find, count distinct roots at the end)
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check("two components", count_components(5, [[0, 1], [1, 2], [3, 4]]), 2)
    check("one component", count_components(5, [[0, 1], [1, 2], [2, 3], [3, 4]]), 1)
