class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reorder_list(head) -> None:
    # TODO: implement (find middle, reverse second half, merge alternately)
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
    head1 = build_list([1, 2, 3, 4])
    reorder_list(head1)
    check("even length", to_values(head1), [1, 4, 2, 3])

    head2 = build_list([1, 2, 3, 4, 5])
    reorder_list(head2)
    check("odd length", to_values(head2), [1, 5, 2, 4, 3])
