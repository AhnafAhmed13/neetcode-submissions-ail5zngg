class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        def is_vowel_word(word):
            vowels = {"a", "e", "i", "o", "u"}
            return word[0] in vowels and word[-1] in vowels
        
        prefix = [0]
        for word in words:
            prefix.append(prefix[-1] + int(is_vowel_word(word)))

        ans = []
        for l, r in queries:
            ans.append(prefix[r+1]-prefix[l])
        
        return ans