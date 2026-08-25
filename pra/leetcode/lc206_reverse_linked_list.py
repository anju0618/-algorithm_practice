class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_list(head):
    # TODO: implement (iterative pointer reversal)
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
    check("basic", to_values(reverse_list(build_list([1, 2, 3, 4, 5]))), [5, 4, 3, 2, 1])
    check("two elements", to_values(reverse_list(build_list([1, 2]))), [2, 1])
    check("empty list", to_values(reverse_list(build_list([]))), [])
