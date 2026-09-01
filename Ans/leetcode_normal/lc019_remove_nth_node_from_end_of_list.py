class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def remove_nth_from_end(head, n: int):
    values = []
    node = head
    while node:
        values.append(node.val)
        node = node.next

    remove_index = len(values) - n
    new_values = values[:remove_index] + values[remove_index + 1:]

    dummy = ListNode()
    curr = dummy
    for v in new_values:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next
