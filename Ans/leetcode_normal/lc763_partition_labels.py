def partition_labels(s: str) -> list[int]:
    last_index = {}
    for i, ch in enumerate(s):
        last_index[ch] = i

    result = []
    start = 0
    end = 0
    for i, ch in enumerate(s):
        if last_index[ch] > end:
            end = last_index[ch]
        if i == end:
            result.append(end - start + 1)
            start = end + 1

    return result
