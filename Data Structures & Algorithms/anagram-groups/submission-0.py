class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagrams = {}
        for index in range(len(strs)):
            word = "".join(sorted(strs[index]))
            if word in anagrams:
                anagrams[word].append(strs[index])
            else:
                anagrams[word] = [strs[index]]
        
        res = []
        for sublist in anagrams.values():
            res.append(sublist)

        return res
        