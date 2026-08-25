class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def add_two_numbers(l1, l2):
    # TODO: implement (digit-by-digit addition with carry)
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
    check("basic", to_values(add_two_numbers(build_list([2, 4, 3]), build_list([5, 6, 4]))), [7, 0, 8])
    check("zeros", to_values(add_two_numbers(build_list([0]), build_list([0]))), [0])
    check("carry propagation", to_values(add_two_numbers(build_list([9, 9, 9, 9, 9, 9, 9]), build_list([9, 9, 9, 9]))), [8, 9, 9, 9, 0, 0, 0, 1])
