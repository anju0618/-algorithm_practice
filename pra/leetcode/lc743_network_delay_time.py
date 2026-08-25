def network_delay_time(times: list[list[int]], n: int, k: int) -> int:
    # TODO: implement (Dijkstra with a hand-rolled min-heap, no heapq)
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check("basic", network_delay_time([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2), 2)
    check("single edge reachable", network_delay_time([[1, 2, 1]], 2, 1), 1)
    check("unreachable", network_delay_time([[1, 2, 1]], 2, 2), -1)
