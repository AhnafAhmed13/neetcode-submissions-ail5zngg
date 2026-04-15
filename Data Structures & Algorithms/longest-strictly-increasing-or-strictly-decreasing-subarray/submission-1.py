class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        res = 1
        curr = 1
        inc = nums[0] < nums[1]
        print("i\t\t[i]\t\t[i+1]\tinc\t\t\tcur\t\tres")
        for i in range(len(nums) - 1):
            if inc:
                if nums[i] < nums[i + 1]:
                    curr += 1
                else:
                    res = max(res, curr)
                    curr = 1
                    if nums[i] > nums[i + 1]:
                        inc = False
                        curr = 2
            else:
                if nums[i] > nums[i + 1]:
                    curr += 1
                else:
                    res = max(res, curr)
                    curr = 1
                    if nums[i] < nums[i + 1]:
                        inc = True
                        curr = 2
            print(i, nums[i], nums[i + 1], inc, curr, res, sep="\t\t")
        return max(res, curr)
