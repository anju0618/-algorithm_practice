class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_k_group(head, k: int):
    values = []
    node = head
    while node:
        values.append(node.val)
        node = node.next

    result = []
    i = 0
    while i < len(values):
        chunk = values[i:i + k]
        if len(chunk) == k:
            chunk = chunk[::-1]
        result.extend(chunk)
        i += k

    dummy = ListNode()
    curr = dummy
    for v in result:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next
