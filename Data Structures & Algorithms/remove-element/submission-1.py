class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        # idxs = []

        # for i in range(len(nums)):
        #     if nums[i] == val:
        #         idxs.append(i)

        # offset = 0
        # for idx in idxs:
        #     nums.pop(idx - offset)
        #     offset += 1

        # return len(nums)

        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k