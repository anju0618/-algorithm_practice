class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_list(head):
    values = []
    node = head
    while node:
        values.append(node.val)
        node = node.next

    dummy = ListNode()
    tail = dummy
    for v in range(len(values) - 1, -1, -1):
        tail.next = ListNode(values[v])
        tail = tail.next
    return dummy.next
