def pattern_tracker(text: str) -> int:
    if len(text) < 2:
        return 0

    count = 0
    for i in range(len(text) - 1):
        ch1 = text[i]
        ch2 = text[i + 1]
        if ch1.isdigit() and ch2.isdigit():
            if int(ch2) == int(ch1) + 1:
                count += 1
    return count
