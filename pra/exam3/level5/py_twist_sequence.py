def twist_sequence(arr: list[int], k: int) -> list[int]:
    # TODO: implement
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check("basic rotation", twist_sequence([1, 2, 3, 4, 5], 2), [4, 5, 1, 2, 3])
    check("rotate by 1", twist_sequence([1, 2, 3], 1), [3, 1, 2])
    check("rotate by 0", twist_sequence([1, 2, 3, 4], 0), [1, 2, 3, 4])
    check("k larger than length", twist_sequence([1, 2, 3], 5), [2, 3, 1])
    check("empty array", twist_sequence([], 3), [])
