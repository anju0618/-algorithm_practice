def can_finish(num_courses: int, prerequisites: list[list[int]]) -> bool:
    # TODO: implement (Kahn's algorithm topological sort)
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check("no cycle", can_finish(2, [[1, 0]]), True)
    check("cycle", can_finish(2, [[1, 0], [0, 1]]), False)
