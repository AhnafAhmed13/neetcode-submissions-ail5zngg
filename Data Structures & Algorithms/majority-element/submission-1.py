class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        # count = Counter(nums)

        # for num, freq in count.items():
        #     if freq >= len(nums) // 2:
        #         return num

        nums.sort()

        curr_size = 1

        for i in range(1, len(nums)):
            if nums[i - 1] == nums[i]:
                curr_size += 1
            else:
                if curr_size > len(nums) // 2:
                    return nums[i - 1]
                curr_size = 1
            
        if curr_size > len(nums) // 2:
            return nums[-1]
        


