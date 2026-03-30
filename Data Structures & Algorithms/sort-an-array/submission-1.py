class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        # Bubble sort
        for i in range(len(nums) - 1):
            swaps = 0
            for j in range(len(nums) - 1 - i):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                    swaps += 1
            if swaps == 0:
                break
        return nums


        # Insertion sort
        # for i in range(len(nums)):
        #     for j in range(i, 0, -1):
        #         if nums[j - 1] > nums[j]:
        #             nums[j - 1], nums[j] = nums[j], nums[j - 1]
        #         else:
        #             break
        # return nums

        # Selection sort
        # for i in range(len(nums)):
        #     curr_min = i
        #     for j in range(i + 1, len(nums)):
        #         if nums[j] < nums[curr_min]:
        #             curr_min = j
        #     nums[i], nums[curr_min] = nums[curr_min], nums[i]
        # return nums