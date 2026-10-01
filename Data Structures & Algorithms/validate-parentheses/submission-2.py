class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            if ch in {"(", "{", "["}:
                stack.append(ch)
            elif ch == ")":
                if not stack or stack[-1] != "(": return False
                stack.pop(-1)
            elif ch == "}":
                if not stack or stack[-1] != "{": return False
                stack.pop(-1)
            elif ch == "]":
                if not stack or stack[-1] != "[": return False
                stack.pop(-1)
        return len(stack) == 0