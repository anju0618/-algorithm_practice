def swim_in_water(grid: list[list[int]]) -> int:
    # TODO: implement (Dijkstra-style: always expand the lowest-elevation frontier cell)
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check("basic", swim_in_water([[0, 2], [1, 3]]), 3)
    check("larger grid", swim_in_water([[0, 1, 2, 3, 4], [24, 23, 22, 21, 5], [12, 13, 14, 15, 16], [11, 17, 18, 19, 20], [10, 9, 8, 7, 6]]), 16)
