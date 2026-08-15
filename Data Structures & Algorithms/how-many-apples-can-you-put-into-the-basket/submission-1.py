class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        weight.sort()
        curr_weight = 0
        i = 0
        while i < len(weight) and (5000 - curr_weight) >= weight[i]:
            curr_weight += weight[i]
            i += 1
        return i