def array_rotation_detector(arr1: list, arr2: list) -> bool:
    # TODO: implement
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check("right rotation", array_rotation_detector([1, 2, 3, 4, 5], [4, 5, 1, 2, 3]), True)
    check("left rotation", array_rotation_detector([1, 2, 3, 4, 5], [5, 1, 2, 3, 4]), True)
    check("reversed, not rotation", array_rotation_detector([1, 2, 3], [3, 2, 1]), False)
    check("length mismatch", array_rotation_detector([1, 2], [1, 2, 3]), False)
    check("both empty", array_rotation_detector([], []), True)
