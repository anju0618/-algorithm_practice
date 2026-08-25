def length_of_lis(nums: list[int]) -> int:
    # TODO: implement (O(n log n) patience sorting with binary search, no sorted())
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check("basic", length_of_lis([10, 9, 2, 5, 3, 7, 101, 18]), 4)
    check("with duplicates", length_of_lis([0, 1, 0, 3, 2, 3]), 4)
    check("all same", length_of_lis([7, 7, 7, 7, 7, 7, 7]), 1)
