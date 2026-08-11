class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        name_heights = list(zip(names, heights))
        name_heights.sort(reverse=True, key=lambda x: x[1])
        return [name for name, height in name_heights]