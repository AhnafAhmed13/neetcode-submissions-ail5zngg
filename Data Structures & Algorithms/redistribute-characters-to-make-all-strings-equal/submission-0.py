class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        # count char freq for all strings
        hm = {}
        for word in words:
            for ch in word:
                if ch not in hm:
                    hm[ch] = 0
                hm[ch] += 1

        for ch in hm:
            if hm[ch] % len(words) != 0:
                return False

        return True