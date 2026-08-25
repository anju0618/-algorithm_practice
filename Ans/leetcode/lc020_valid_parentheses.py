def is_valid_parentheses(s: str) -> bool:
    stack = []
    closing_to_opening = {")": "(", "]": "[", "}": "{"}
    opening = ("(", "[", "{")

    for ch in s:
        if ch in opening:
            stack.append(ch)
        elif ch in closing_to_opening:
            if not stack or stack.pop() != closing_to_opening[ch]:
                return False
        else:
            return False  # LeetCode版は括弧以外の文字は入力に含まれない前提
    return len(stack) == 0
