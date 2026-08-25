def constellation_mapper(stars: list[tuple[int, int]], size: int) -> list[str]:
    # TODO: implement
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check("diagonal", constellation_mapper([(0, 0), (1, 1), (2, 2)], 3), ["*..", ".*.", "..*"])
    check("with duplicate", constellation_mapper([(0, 0), (0, 1), (0, 2), (1, 1), (2, 2)], 3), ["***", ".*.", "..*"])
    check("out of bounds ignored", constellation_mapper([(0, 0), (5, 5), (2, 2)], 3), ["*..", "...", "..*"])
    check("small grid", constellation_mapper([(0, 0), (5, 5)], 2), ["*.", ".."])
