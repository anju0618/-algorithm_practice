def course_order(courses: dict[str, list[str]]) -> list[str]:
    # TODO: implement Kahn's algorithm
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check("simple chain", course_order({"app": ["database"], "database": ["driver"], "driver": []}), ["driver", "database", "app"])
    check("circular dependency", course_order({"X": ["Y"], "Y": ["X"]}), [])
