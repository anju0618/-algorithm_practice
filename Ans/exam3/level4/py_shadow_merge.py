def shadow_merge(list1: list[int], list2: list[int]) -> list[int]:
    result = []
    i, j = 0, 0
    len1, len2 = len(list1), len(list2)
    while i < len1 and j < len2:
        if list1[i] <= list2[j]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1
    if i < len1:
        result.extend(list1[i:])
    if j < len2:
        result.extend(list2[j:])
    return result
