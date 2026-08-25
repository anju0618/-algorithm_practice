class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        # TODO: implement (hand-rolled min-heap of size k, no heapq)
        pass

    def add(self, val: int) -> int:
        pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    kl = KthLargest(3, [4, 5, 8, 2])
    check("add 3", kl.add(3), 4)
    check("add 5", kl.add(5), 5)
    check("add 10", kl.add(10), 5)
    check("add 9", kl.add(9), 8)
    check("add 4", kl.add(4), 8)
