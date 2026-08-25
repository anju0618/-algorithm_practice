class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def has_cycle(head) -> bool:
    # TODO: implement (Floyd's cycle detection, slow/fast pointers)
    pass


def build_cyclic_list(values, pos):
    if not values:
        return None
    nodes = [ListNode(v) for v in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    if pos != -1:
        nodes[-1].next = nodes[pos]
    return nodes[0]


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check("has cycle", has_cycle(build_cyclic_list([3, 2, 0, -4], 1)), True)
    check("no cycle", has_cycle(build_cyclic_list([1, 2], -1)), False)
    check("empty list", has_cycle(build_cyclic_list([], -1)), False)
