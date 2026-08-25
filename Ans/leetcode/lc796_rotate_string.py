def rotate_string(s: str, goal: str) -> bool:
    if len(s) != len(goal):
        return False
    if not s:
        return True

    n = len(s)
    for start in range(n):
        match = True
        for i in range(n):
            if s[(start + i) % n] != goal[i]:
                match = False
                break
        if match:
            return True
    return False
