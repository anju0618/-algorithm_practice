def max_area_of_island(grid: list[list[int]]) -> int:
    # TODO: implement (DFS returning the area of the island it sinks)
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check("basic", max_area_of_island([[0, 0, 1, 0], [0, 1, 1, 0], [0, 0, 0, 1]]), 3)
    check("no land", max_area_of_island([[0, 0, 0], [0, 0, 0]]), 0)
