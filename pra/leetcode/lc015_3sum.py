def three_sum(nums: list[int]) -> list[list[int]]:
    # TODO: implement without sorted()/.sort()
    pass


def normalize(triplets):
    # テスト比較専用（Ans側の実装にsorted()を使うわけではない）
    return sorted(tuple(sorted(t)) for t in triplets)


def check(label, actual, expected):
    ok = normalize(actual) == normalize(expected)
    status = "[OK]" if ok else "[NG]"
    print(f"{status} {label}")
    if not ok:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check("basic", three_sum([-1, 0, 1, 2, -1, -4]), [[-1, -1, 2], [-1, 0, 1]])
    check("no valid triplet", three_sum([0, 1, 1]), [])
    check("all zeros", three_sum([0, 0, 0]), [[0, 0, 0]])
