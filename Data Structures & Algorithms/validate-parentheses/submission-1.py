class Solution:
    def isValid(self, s: str) -> bool:

        # edge case
        if len(s) % 2 != 0:
            return False

        stack = []
        for bracket in s:
            if bracket in ['(', '{', '[']:
                stack.insert(0, bracket)
            else:
                if len(stack) == 0:
                    return False

                opening = stack.pop(0)
                if bracket == ')' and opening != '('\
                or bracket == '}' and opening != '{'\
                or bracket == ']' and opening != '[':
                    return False
        
        if len(stack) > 0:
            return False
            
        return True
        