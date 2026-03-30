class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        out = []
        for i in range(len(nums)):
            left, right = 1, 1
            for j in range(i):
                left *= nums[j]
            for j in range(i+1, len(nums)):
                right *= nums[j]
            out.append(left * right)
        
        return out
        