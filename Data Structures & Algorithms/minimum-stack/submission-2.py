class MinStack:

    def __init__(self):
        self.stack = []
        self.prefix = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.prefix:
            self.prefix.append(val)
        else:
            self.prefix.append(min(val, self.prefix[-1]))

    def pop(self) -> None:
        self.stack.pop(-1)
        self.prefix.pop(-1)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.prefix[-1]
