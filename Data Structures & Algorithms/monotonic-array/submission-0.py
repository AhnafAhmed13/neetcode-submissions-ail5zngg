class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        inc = sorted(nums)
        dec = inc[::-1]
        print(nums)
        print(inc)
        print(dec)
        flag = True
        for i in range(len(nums)):
            if nums[i] != inc[i]:
                flag = False
                break
        if flag:
            return True
        for i in range(len(nums)):
            if nums[i] != dec[i]:
                flag = False
                break
        else:
            flag = True
        return flag