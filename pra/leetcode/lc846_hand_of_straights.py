def is_n_straight_hand(hand: list[int], group_size: int) -> bool:
    # TODO: implement (count values, always start a group from the smallest remaining value)
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check("basic", is_n_straight_hand([1, 2, 3, 6, 2, 3, 4, 7, 8], 3), True)
    check("cannot form groups", is_n_straight_hand([1, 2, 3, 4, 5], 4), False)
