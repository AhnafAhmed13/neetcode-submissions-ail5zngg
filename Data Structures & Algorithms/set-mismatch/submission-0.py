class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        res = [0, 0]
        n = len(nums)

        for i in range(1, n + 1):
            cnt = 0
            for num in nums:
                if num == i:
                    cnt += 1

            if cnt == 0:
                res[1] = i
            elif cnt == 2:
                res[0] = i

        return res