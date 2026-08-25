def merge_triplets(triplets: list[list[int]], target: list[int]) -> bool:
    # TODO: implement (ignore triplets that exceed target; track which target positions are matchable)
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check("basic", merge_triplets([[2, 5, 3], [1, 8, 4], [1, 7, 5]], [2, 7, 5]), True)
    check("missing value", merge_triplets([[3, 4, 5], [4, 5, 6]], [3, 2, 5]), False)
    check("multiple triplets needed", merge_triplets([[2, 5, 3], [2, 3, 4], [1, 2, 5], [5, 2, 3]], [5, 5, 5]), True)
