# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        if not pairs:
            return []
        states = [pairs[:]]
        for i in range(1, len(pairs)):
            curr = states[-1][:]
            j = i
            while j > 0:
                if curr[j - 1].key > curr[j].key:
                    curr[j - 1], curr[j] = curr[j], curr[j - 1]
                    j -= 1
                else:
                    break
            states.append(curr)
        return states