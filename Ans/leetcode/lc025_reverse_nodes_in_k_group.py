class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_k_group(head, k: int):
    # まずk個先まで進めるノードがあるか確認する
    node = head
    count = 0
    while node and count < k:
        node = node.next
        count += 1
    if count < k:
        return head  # 残りがk個未満ならそのまま

    # 先頭k個を反転する
    prev = reverse_k_group(node, k)  # k個より後ろを先に処理した結果を繋ぎ先にする
    curr = head
    for _ in range(k):
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev
