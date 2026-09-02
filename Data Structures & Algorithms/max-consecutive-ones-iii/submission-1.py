class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = res = zs = 0; lz = -1
        for r in range(len(nums)):
            if nums[r] == 0:
                if lz == -1: lz = r
                zs += 1
                if zs > k:
                    zs -= 1; tmp = i = lz + 1
                    while i < len(nums) and nums[i] != 0: i += 1
                    lz = i; l = min(tmp, lz)
            curr = r - l + 1
            res = max(res, curr)
        return res
