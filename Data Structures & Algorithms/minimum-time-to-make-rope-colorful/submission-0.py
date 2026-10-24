class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        res = 0
        l = 0
        for r in range(1, len(colors)):
            if colors[r] != colors[r - 1]:
                if l < r - 1:
                    res += sum(sorted(neededTime[l:r])[:r-l-1])
                l = r
        
        if l < len(colors) - 1:
            # time = neededTime[l:r+1]; print(time)
            # time.sort(); print(time)
            # time = time[:len(time) - 1]; print(time)
            # time = sum(time); print(time)
            # res += time; print(res)
            res += sum(sorted(neededTime[l:len(colors)])[:len(colors)-l-1])

        return res
