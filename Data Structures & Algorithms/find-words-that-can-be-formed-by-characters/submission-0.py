class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        from collections import Counter
        charmap = Counter(chars)
        res = 0
        for word in words:
            word_char = Counter(word)
            if len(word_char) > len(charmap):
                continue

            for ch, freq in word_char.items():
                if ch not in charmap or charmap[ch] < freq:
                    break
            else:
                res += len(word)
        return res