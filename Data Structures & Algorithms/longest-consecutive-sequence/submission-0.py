class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # make set
        nums = set(nums)

        # iterate and find the start of each sequence
        res = 0
        for num in nums:
            # check if start of the sequence (left doesn't exist)
            if (num - 1) not in nums:
                curr = 1
                next_num = num + 1
                while next_num in nums:
                    curr += 1
                    next_num += 1
                res = max(res, curr)
        return res        
        