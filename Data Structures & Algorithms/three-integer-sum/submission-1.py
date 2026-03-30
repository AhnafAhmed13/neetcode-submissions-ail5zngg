class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        
        # Sort input array
        nums.sort()

        # Iterate over all elts
        # anchor at a
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue # skip if duplicate
            # 2 pointers
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1 # decrease
                elif threeSum < 0:
                    l += 1 # increase
                else:
                    res.append([a, nums[l], nums[r]]) # found
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1 # skip if duplicate
        return res