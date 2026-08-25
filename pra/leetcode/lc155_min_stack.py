class MinStack:
    def __init__(self):
        # TODO: implement
        pass

    def push(self, value: int) -> None:
        pass

    def pop(self) -> None:
        pass

    def top(self) -> int:
        pass

    def get_min(self) -> int:
        pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    s = MinStack()
    s.push(-2)
    s.push(0)
    s.push(-3)
    check("min after 3 pushes", s.get_min(), -3)
    s.pop()
    check("top after pop", s.top(), 0)
    check("min after pop", s.get_min(), -2)
