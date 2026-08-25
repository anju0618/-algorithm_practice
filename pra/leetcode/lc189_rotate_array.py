def rotate_array(nums: list[int], k: int) -> list[int]:
    # TODO: implement
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check("basic", rotate_array([1, 2, 3, 4, 5, 6, 7], 3), [5, 6, 7, 1, 2, 3, 4])
    check("negative numbers", rotate_array([-1, -100, 3, 99], 2), [3, 99, -1, -100])
