def find_redundant_connection(edges: list[list[int]]) -> list[int]:
    # TODO: implement (Union-Find; the edge that first connects an already-connected pair is redundant)
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check("basic", find_redundant_connection([[1, 2], [1, 3], [2, 3]]), [2, 3])
    check("longer cycle", find_redundant_connection([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]), [1, 4])
