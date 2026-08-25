class TimeMap:
    def __init__(self):
        # TODO: implement
        pass

    def set(self, key: str, value: str, timestamp: int) -> None:
        pass

    def get(self, key: str, timestamp: int) -> str:
        pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    tm = TimeMap()
    tm.set("foo", "bar", 1)
    check("exact timestamp", tm.get("foo", 1), "bar")
    check("later timestamp, same value", tm.get("foo", 3), "bar")
    tm.set("foo", "bar2", 4)
    check("updated value", tm.get("foo", 4), "bar2")
    check("after update", tm.get("foo", 5), "bar2")
