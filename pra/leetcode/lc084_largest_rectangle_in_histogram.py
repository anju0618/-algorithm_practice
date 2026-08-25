def largest_rectangle_area(heights: list[int]) -> int:
    # TODO: implement with a monotonic stack
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check("basic", largest_rectangle_area([2, 1, 5, 6, 2, 3]), 10)
    check("two bars", largest_rectangle_area([2, 4]), 4)
