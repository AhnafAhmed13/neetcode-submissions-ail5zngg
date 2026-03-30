class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        # Insertion sort

        for i in range(len(nums)):
            curr_min = i
            for j in range(i + 1, len(nums)):
                if nums[j] < nums[curr_min]:
                    curr_min = j

            nums[i], nums[curr_min] = nums[curr_min], nums[i]

        return nums