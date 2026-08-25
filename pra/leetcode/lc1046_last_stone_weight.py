def last_stone_weight(stones: list[int]) -> int:
    # TODO: implement (hand-rolled max-heap via negated values, no heapq)
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check("basic", last_stone_weight([2, 7, 4, 1, 8, 1]), 1)
    check("single stone", last_stone_weight([1]), 1)
