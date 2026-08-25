def oranges_rotting(grid: list[list[int]]) -> int:
    # TODO: implement (multi-source BFS from all initially rotten oranges)
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check("basic", oranges_rotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]), 4)
    check("unreachable fresh orange", oranges_rotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]]), -1)
    check("no fresh oranges", oranges_rotting([[0, 2]]), 0)
