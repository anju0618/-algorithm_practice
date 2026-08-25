def min_cost_connect_points(points: list[list[int]]) -> int:
    # TODO: implement (Prim's algorithm with a hand-rolled min-heap, no heapq)
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check("basic", min_cost_connect_points([[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]), 20)
    check("negative coordinates", min_cost_connect_points([[3, 12], [-2, 5], [-4, 1]]), 18)
