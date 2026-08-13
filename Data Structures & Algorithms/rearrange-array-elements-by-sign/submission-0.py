class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = []
        neg = []
        for n in nums:
            if n < 0:
                neg.append(n)
            else:
                pos.append(n)
        res = []
        for i in range(len(pos)):
            res.append(pos[i])
            res.append(neg[i])
        return res