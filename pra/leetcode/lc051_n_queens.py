def solve_n_queens(n: int) -> list[list[str]]:
    # TODO: implement (backtracking with column/diagonal occupancy tracking)
    pass


def normalize(boards):
    return sorted(tuple(b) for b in boards)


def check(label, actual, expected):
    ok = normalize(actual) == normalize(expected)
    status = "[OK]" if ok else "[NG]"
    print(f"{status} {label}")
    if not ok:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check("n=4", solve_n_queens(4), [[".Q..", "...Q", "Q...", "..Q."], ["..Q.", "Q...", "...Q", ".Q.."]])
    check("n=1", solve_n_queens(1), [["Q"]])
