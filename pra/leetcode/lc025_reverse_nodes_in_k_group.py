class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_k_group(head, k: int):
    # TODO: implement (reverse each group of k, recurse on the rest)
    pass


def build_list(values):
    dummy = ListNode()
    tail = dummy
    for v in values:
        tail.next = ListNode(v)
        tail = tail.next
    return dummy.next


def to_values(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


def check(label, actual, expected):
    status = "[OK]" if actual == expected else "[NG]"
    print(f"{status} {label}")
    if actual != expected:
        print(f"      got:      {actual}")
        print(f"      expected: {expected}")


if __name__ == "__main__":
    check("k=2", to_values(reverse_k_group(build_list([1, 2, 3, 4, 5]), 2)), [2, 1, 4, 3, 5])
    check("k=3", to_values(reverse_k_group(build_list([1, 2, 3, 4, 5]), 3)), [3, 2, 1, 4, 5])
