class MinStack:
    def __init__(self):
        self._stack = []
        self._min_stack = []  # min_stack[i] = min of stack[0..i]

    def push(self, value: int) -> None:
        self._stack.append(value)
        if not self._min_stack or value <= self._min_stack[-1]:
            self._min_stack.append(value)
        else:
            self._min_stack.append(self._min_stack[-1])

    def pop(self) -> None:
        self._stack.pop()
        self._min_stack.pop()

    def top(self) -> int:
        return self._stack[-1]

    def get_min(self) -> int:
        return self._min_stack[-1]
