class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = [(temperatures[0], 0)]
        res = [0] * len(temperatures)

        for i in range(1, len(temperatures)):
            
            while stack and stack[-1][0] < temperatures[i]:

                _, idx = stack.pop()

                res[idx] = i - idx
            
            stack.append((temperatures[i], i))

        return res


        
        
        
        
        
        
        
        
        
        
        
        
        # n = len(temperatures)
        # res = [0] * n

        # r = n - 1
        # l = r - 1
        # while r > 0:
        #     l = r - 1
        #     while temperatures[l] < temperatures[r]:
        #         res[l] = r - l
        #         l -= 1
        #     r -= 1
        # res[-1] = 0
        # return res