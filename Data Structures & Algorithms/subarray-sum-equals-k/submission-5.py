class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        prefix = { 0 : 1 }
        res = 0

        # prefix sum
        curr_sum = 0
        for num in nums:
            # update running sum
            curr_sum += num

            # find diff from k
            diff = curr_sum - k
            # check if a possible prefix subarray exists that is equal to the diff to make the curr sum equal to k
            res += prefix.get(diff, 0)

            # add curr_sum as a prefix sum to the hash map, increment its count
            prefix[curr_sum] = prefix.get(curr_sum, 0) + 1

            # THIS ORDER MATTERS: DON'T ADD TO HASH MAP BEFORE ADDING TO RES
        return res






        # brute force
        # for i in range(n):
        #     for j in range(i, n):
        #         s = sum(nums[i:j+1])
        #         # print(i, j, s)
        #         if s == k:
        #             res += 1
        # return res
        