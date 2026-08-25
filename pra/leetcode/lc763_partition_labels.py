def partition_labels(s: str) -> list[int]:
    # TODO: implement (track each char's last occurrence, extend the current part greedily)
    pass


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check("basic", partition_labels("ababcbacadefegdehijhklij"), [9, 7, 8])
    check("single part", partition_labels("eccbbbbdec"), [10])
