def package_dependency_resolver(packages: dict[str, list[str]]) -> list[str]:
    # TODO: implement Kahn's algorithm without sorted()/.sort()
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check("simple chain", package_dependency_resolver({"app": ["database"], "database": ["driver"], "driver": []}), ["driver", "database", "app"])
    check("diamond", package_dependency_resolver({"A": [], "B": ["A"], "C": ["A", "B"]}), ["A", "B", "C"])
    check("empty input", package_dependency_resolver({}), [])
    check("circular dependency", package_dependency_resolver({"X": ["Y"], "Y": ["X"]}), [])
    check("wave tie-break", package_dependency_resolver({"web": [], "api": [], "frontend": ["web"], "backend": ["api"]}), ["api", "web", "backend", "frontend"])
