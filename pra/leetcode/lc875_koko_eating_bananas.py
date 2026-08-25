def min_eating_speed(piles: list[int], h: int) -> int:
    # TODO: implement (binary search on the answer speed)
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check("basic", min_eating_speed([3, 6, 7, 11], 8), 4)
    check("tight deadline", min_eating_speed([30, 11, 23, 4, 20], 5), 30)
    check("looser deadline", min_eating_speed([30, 11, 23, 4, 20], 6), 23)
