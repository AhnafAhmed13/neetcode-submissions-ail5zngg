class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        idxs = {n: i for i, n in enumerate(nums2)}
        res = []
        for n1 in nums1:
            idx = idxs[n1]
            for n2 in nums2[idx:]:
                if n2 > n1:
                    res.append(n2)
                    break
            else:
                res.append(-1)
        return res