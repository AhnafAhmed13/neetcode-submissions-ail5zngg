class Solution:
    def specialArray(self, nums: List[int]) -> int:
        if len(nums) == 1 and nums[0] != 0:
            return 1

        nums.sort()

        idx = {}

        for i, n in enumerate(nums):
            if n not in idx:
                idx[n] = i

        # print(idx)

        ns = sorted(idx.keys())
        
        # print(ns)

        n = 2
        i = 0
        while n <= len(nums) - idx[ns[i]]:
            while i < len(ns) and n > ns[i]:
                i += 1
            if i == len(ns):
                return -1
            # print(n, len(nums) - idx[ns[i]])
            if n == len(nums) - idx[ns[i]]:
                return n
            
            n += 1
        
        return -1
