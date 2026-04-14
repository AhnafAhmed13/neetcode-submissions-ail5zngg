class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        idxs = {n: i for i, n in enumerate(nums2)}
        res = []
        no_greater_after = set()
        mx = nums2[-1]
        for i in range(len(nums2) - 1, -1, -1):
            if nums2[i] >= mx:
                no_greater_after.add(nums2[i])
                mx = nums2[i]
                
        for n1 in nums1:
            if n1 in no_greater_after:
                res.append(-1)
                continue
            for n2 in nums2[idxs[n1]:]:
                if n2 > n1:
                    res.append(n2)
                    break
        return res