def car_fleet(target: int, position: list[int], speed: list[int]) -> int:
    n = len(position)
    if n == 0:
        return 0

    pairs = list(zip(position, speed))
    # targetに近い(=positionが大きい)順に並べる。挿入ソートで手書き（sorted()は使わない）
    for i in range(1, n):
        key = pairs[i]
        j = i - 1
        while j >= 0 and pairs[j][0] < key[0]:
            pairs[j + 1] = pairs[j]
            j -= 1
        pairs[j + 1] = key

    fleets = 0
    current_time = 0.0
    for pos, spd in pairs:
        time = (target - pos) / spd
        if time > current_time:
            # 前の車列に追いつけない = 新しい車列
            fleets += 1
            current_time = time
        # 追いつける場合は前の車列に吸収される（current_timeは更新しない）
    return fleets
