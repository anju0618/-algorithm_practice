def eval_rpn(tokens: list[str]) -> int:
    stack = []
    operators = ("+", "-", "*", "/")

    for tok in tokens:
        if tok in operators:
            b = stack.pop()
            a = stack.pop()
            if tok == "+":
                stack.append(a + b)
            elif tok == "-":
                stack.append(a - b)
            elif tok == "*":
                stack.append(a * b)
            else:
                stack.append(int(a / b))  # int()はゼロ方向への切り捨て
        else:
            stack.append(int(tok))
    return stack[0]
