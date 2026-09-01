def can_complete_circuit(gas: list[int], cost: list[int]) -> int:
    n = len(gas)

    for start in range(n):
        tank = 0
        made_it = True
        for step in range(n):
            i = (start + step) % n
            tank += gas[i] - cost[i]
            if tank < 0:
                made_it = False
                break
        if made_it:
            return start

    return -1
