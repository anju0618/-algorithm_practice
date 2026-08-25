def k_closest(points: list[list[int]], k: int) -> list[list[int]]:
    # TODO: implement (hand-rolled max-heap of size k, no heapq)
    pass


def check(label, actual, expected):
    ok = sorted(map(tuple, actual)) == sorted(map(tuple, expected))
    status = "[OK]" if ok else "[NG]"
    print(f"{status} {label}")
    if not ok:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check("k=1", k_closest([[1, 3], [-2, 2]], 1), [[-2, 2]])
    check("k=2", k_closest([[3, 3], [5, -1], [-2, 4]], 2), [[3, 3], [-2, 4]])
