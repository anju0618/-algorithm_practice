def merge_triplets(triplets: list[list[int]], target: list[int]) -> bool:
    achievable = [False, False, False]

    for t in triplets:
        if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
            continue  # このtripletはどれかの成分がtargetを超えている＝使うと壊れる
        for i in range(3):
            if t[i] == target[i]:
                achievable[i] = True

    return achievable[0] and achievable[1] and achievable[2]
