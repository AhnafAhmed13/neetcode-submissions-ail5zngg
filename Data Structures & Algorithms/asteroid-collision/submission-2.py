class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        stack = []

        for i in range(len(asteroids)):
            if not stack:
                stack.append(asteroids[i])
            else:
                if asteroids[i] < 0:
                    while stack:
                        if stack[-1] > 0:
                            if stack[-1] < abs(asteroids[i]):
                                stack.pop()
                            elif stack[-1] > abs(asteroids[i]):
                                break
                            else:
                                stack.pop()
                                break
                        else:
                            stack.append(asteroids[i])
                            break
                    else:
                        stack.append(asteroids[i])
                else:
                    stack.append(asteroids[i])
        return stack