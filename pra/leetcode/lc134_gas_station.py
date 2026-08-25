def can_complete_circuit(gas: list[int], cost: list[int]) -> int:
    # TODO: implement (greedy: reset the candidate start whenever the running tank goes negative)
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check("basic", can_complete_circuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]), 3)
    check("impossible", can_complete_circuit([2, 3, 4], [3, 4, 3]), -1)
