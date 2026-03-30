class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def next(j):
            while j < len(nums):
                if nums[j] != 0:
                    break
                j += 1
            if j >= len(nums):
                return -1
            return j

        i = 0
        j = next(0)
        if j == -1:
            return

        while i < len(nums):
            # print(nums, i, j)
            if nums[i] == 0:
                j = next(max(i, j))
                if j == -1:
                    return
                nums[i], nums[j] = nums[j], nums[i]
            i += 1

        return
                    

                    