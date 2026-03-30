class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        for t in tokens:

            if t == "+":
                b = stack.pop()
                a = stack.pop()
                sum = a + b
                stack.append(sum)
        
            elif t == "-":
                b = stack.pop()
                a = stack.pop()
                diff = a - b
                stack.append(diff)

            elif t == "*":
                b = stack.pop()
                a = stack.pop()
                prod = a * b
                stack.append(prod)

            elif t == "/":
                b = stack.pop()
                a = stack.pop()
                div = int(a / b)
                stack.append(div)

            else:
                stack.append(int(t))

        return int(stack.pop())