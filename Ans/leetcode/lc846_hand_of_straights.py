def is_n_straight_hand(hand: list[int], group_size: int) -> bool:
    if len(hand) % group_size != 0:
        return False

    counts = {}
    for c in hand:
        counts[c] = counts.get(c, 0) + 1

    def insertion_sort(items):
        arr = list(items)
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr

    starts = insertion_sort(counts.keys())

    for start in starts:
        count = counts[start]
        if count == 0:
            continue
        for k in range(start, start + group_size):
            if counts.get(k, 0) < count:
                return False
            counts[k] -= count

    return True
