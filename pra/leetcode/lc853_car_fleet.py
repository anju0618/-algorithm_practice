def car_fleet(target: int, position: list[int], speed: list[int]) -> int:
    # TODO: implement without sorted() (sort by position descending)
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check("basic", car_fleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]), 3)
    check("single car", car_fleet(10, [3], [3]), 1)
    check("chain merge", car_fleet(100, [0, 2, 4], [4, 2, 1]), 1)
