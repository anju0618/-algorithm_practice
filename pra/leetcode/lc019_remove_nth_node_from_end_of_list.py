class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def remove_nth_from_end(head, n: int):
    # TODO: implement (one pass, two pointers n apart)
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
    check("remove middle", to_values(remove_nth_from_end(build_list([1, 2, 3, 4, 5]), 2)), [1, 2, 3, 5])
    check("remove only node", to_values(remove_nth_from_end(build_list([1]), 1)), [])
    check("remove head", to_values(remove_nth_from_end(build_list([1, 2]), 1)), [1])
