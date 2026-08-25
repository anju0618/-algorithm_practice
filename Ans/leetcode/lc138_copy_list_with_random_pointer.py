class Node:
    def __init__(self, val, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random


def copy_random_list(head):
    if not head:
        return None

    old_to_new = {}  # 元ノード -> コピーノード
    curr = head
    while curr:
        old_to_new[curr] = Node(curr.val)
        curr = curr.next

    curr = head
    while curr:
        old_to_new[curr].next = old_to_new.get(curr.next)
        old_to_new[curr].random = old_to_new.get(curr.random)
        curr = curr.next

    return old_to_new[head]
