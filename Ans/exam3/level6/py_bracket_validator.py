def bracket_validator(s: str) -> bool:
    if s == "":
        return True

    stack = []
    closing_to_opening = {")": "(", "]": "[", "}": "{"}
    opening = ("(", "[", "{")

    for ch in s:
        if ch in opening:
            stack.append(ch)
        elif ch in closing_to_opening:
            if not stack or stack.pop() != closing_to_opening[ch]:
                return False
    return len(stack) == 0
