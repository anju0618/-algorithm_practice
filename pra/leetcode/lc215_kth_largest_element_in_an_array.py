def find_kth_largest(nums: list[int], k: int) -> int:
    # TODO: implement (hand-rolled min-heap of size k, no heapq)
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check("basic", find_kth_largest([3, 2, 1, 5, 6, 4], 2), 5)
    check("with duplicates", find_kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4), 4)
