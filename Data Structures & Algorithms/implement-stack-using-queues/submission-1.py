from collections import deque

class MyStack:

    def __init__(self):
        self.stack1 = deque([])
        self.stack2 = deque([])
        self.top_val = None

    def push(self, x: int) -> None:
        self.stack1.append(x)
        self.top_val = x

    def pop(self) -> int:
        if not self.empty(): # Check if empty
            n = len(self.stack1)
            if n == 1: # If only 1 element
                res = self.stack1.popleft()
                self.top_val = None
                return res

            for _ in range(n - 1): # Dump n - 1 elements to stack2
                self.stack2.append(self.stack1.popleft())
            res = self.stack1.popleft() # Pop top

            for _ in range(n - 2): # Return n - 1 elements to stack1
                self.stack1.append(self.stack2.popleft())
            self.top_val = self.stack2.popleft() # Update top
            self.stack1.append(self.top_val)

            return res

    def top(self) -> int:
        return self.top_val

    def empty(self) -> bool:
        return len(self.stack1) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()