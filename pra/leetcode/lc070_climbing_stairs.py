def climb_stairs(n: int) -> int:
    # TODO: implement (Fibonacci-shaped DP)
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check("n=2", climb_stairs(2), 2)
    check("n=3", climb_stairs(3), 3)
