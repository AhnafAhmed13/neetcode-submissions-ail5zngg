class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        lprod = [nums[0]]
        rprod = [nums[-1]]

        for i in range(1, n):
            lprod.append(lprod[-1] * nums[i])
            rprod.append(rprod[-1] * nums[n - 1 - i])

        rprod = rprod[::-1]

        res = [rprod[1]]
        for i in range(1, n - 1):
            res.append(lprod[i - 1] * rprod[i + 1])

        res.append(lprod[-2])
        return res