class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")
        stack = []
        num = 0
        op = "+"
        for i, ch in enumerate(s):
            if ch.isdigit():
                num = num * 10 + int(ch)
            if (not ch.isdigit()) or i == len(s) - 1:
                if op == "+":
                    stack.append(num)
                elif op == "-":
                    stack.append(-num)
                elif op == "*":
                    top = stack.pop()
                    stack.append(top * num)
                elif op == "/":
                    top = stack.pop()
                    stack.append(int(top / num))
                num = 0
                op = ch
        return sum(stack)