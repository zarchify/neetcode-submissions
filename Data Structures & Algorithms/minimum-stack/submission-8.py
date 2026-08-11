class MinStack:
    def __init__(self):
        self.rep = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.rep.append(val)
        if self.min_stack:
            self.min_stack.append(min(val, self.min_stack[-1]))
        else:
            self.min_stack.append(val)

    def pop(self) -> None:
        self.min_stack.pop()
        return self.rep.pop()

    def top(self) -> int:
        return self.rep[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]