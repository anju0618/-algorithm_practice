def last_stone_weight(stones: list[int]) -> int:
    stones = stones[:]

    def pop_max():
        max_i = 0
        for i in range(1, len(stones)):
            if stones[i] > stones[max_i]:
                max_i = i
        return stones.pop(max_i)

    while len(stones) > 1:
        y = pop_max()
        x = pop_max()
        if y != x:
            stones.append(y - x)

    return stones[0] if stones else 0
