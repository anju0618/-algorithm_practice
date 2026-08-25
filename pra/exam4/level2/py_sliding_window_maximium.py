def sliding_window_maximium(nums: list[int], k: int) -> list[int]:
    # TODO: implement
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check("basic", sliding_window_maximium([1, 3, -1, -3, 5, 3, 6, 7], 3), [3, 3, 5, 5, 6, 7])
    check("window size 2", sliding_window_maximium([4, 2, 12, 11, -5], 2), [4, 12, 12, 11])
    check("empty input", sliding_window_maximium([], 3), [])
