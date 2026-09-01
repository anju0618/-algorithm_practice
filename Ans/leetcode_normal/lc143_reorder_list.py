class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reorder_list(head) -> None:
    if not head:
        return

    nodes = []
    node = head
    while node:
        nodes.append(node)
        node = node.next

    left, right = 0, len(nodes) - 1
    while left < right:
        nodes[left].next = nodes[right]
        left += 1
        if left == right:
            break
        nodes[right].next = nodes[left]
        right -= 1

    nodes[left].next = None
