def list_intersection_finder(lists: list[list[int]]) -> list[int]:
    if not lists:
        return []
    for lst in lists:
        if not lst:
            return []

    result = []
    for value in lists[0]:
        if value in result:
            continue
        in_all = True
        for other in lists[1:]:
            if value not in other:
                in_all = False
                break
        if in_all:
            result.append(value)

    # 挿入ソートで昇順に並べる（sorted()は使わない）
    for i in range(1, len(result)):
        key = result[i]
        j = i - 1
        while j >= 0 and result[j] > key:
            result[j + 1] = result[j]
            j -= 1
        result[j + 1] = key
    return result
