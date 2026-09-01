class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def has_cycle(head) -> bool:
    visited = []
    node = head
    while node:
        if node in visited:  # ListNodeは==を再定義していないので、これは同一オブジェクトかどうかの比較
            return True
        visited.append(node)
        node = node.next
    return False
