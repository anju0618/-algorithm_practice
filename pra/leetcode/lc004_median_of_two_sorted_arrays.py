def find_median_sorted_arrays(nums1: list[int], nums2: list[int]) -> float:
    # TODO: implement (binary search partition, O(log(m+n)))
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check("odd total", find_median_sorted_arrays([1, 3], [2]), 2.0)
    check("even total", find_median_sorted_arrays([1, 2], [3, 4]), 2.5)
