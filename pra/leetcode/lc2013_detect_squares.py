class DetectSquares:
    def __init__(self):
        # TODO: implement (point -> count dict, plus a list of unique points)
        pass

    def add(self, point: list[int]) -> None:
        pass

    def count(self, point: list[int]) -> int:
        pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    ds = DetectSquares()
    ds.add([3, 10])
    ds.add([11, 2])
    ds.add([3, 2])
    check("one square", ds.count([11, 10]), 1)
    check("no square", ds.count([14, 8]), 0)
    ds.add([11, 2])
    check("duplicate point doubles the count", ds.count([11, 10]), 2)
