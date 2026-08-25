class MedianFinder:
    def __init__(self):
        # TODO: implement (two hand-rolled heaps, balanced halves, no heapq)
        pass

    def add_num(self, num: int) -> None:
        pass

    def find_median(self) -> float:
        pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    mf = MedianFinder()
    mf.add_num(1)
    mf.add_num(2)
    check("even count", mf.find_median(), 1.5)
    mf.add_num(3)
    check("odd count", mf.find_median(), 2.0)
