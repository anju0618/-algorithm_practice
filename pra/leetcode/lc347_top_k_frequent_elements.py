def top_k_frequent(nums: list[int], k: int) -> list[int]:
    # TODO: implement without sorted()/heapq
    pass


def check(label, actual, expected):
    status = "[OK]" if set(actual) == set(expected) and len(actual) == len(expected) else "[NG]"
    print(f"{status} {label}")
    if not (set(actual) == set(expected) and len(actual) == len(expected)):
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check("k=2", top_k_frequent([1, 1, 1, 2, 2, 3], 2), [1, 2])
    check("single element", top_k_frequent([1], 1), [1])
    check("larger input", top_k_frequent([1, 2, 1, 2, 1, 2, 3, 1, 3, 2], 2), [1, 2])
