def merge_k_sorted_lists(lists: list[list[int]]) -> list[int]:
    def merge_two(a, b):
        merged = []
        i = j = 0
        while i < len(a) and j < len(b):
            if a[i] <= b[j]:
                merged.append(a[i])
                i += 1
            else:
                merged.append(b[j])
                j += 1
        merged.extend(a[i:])
        merged.extend(b[j:])
        return merged

    result = []
    for lst in lists:
        result = merge_two(result, lst)
    return result
