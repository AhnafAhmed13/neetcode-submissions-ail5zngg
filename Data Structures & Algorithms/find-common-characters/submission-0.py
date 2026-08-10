class Solution:
    from collections import Counter
    def commonChars(self, words: List[str]) -> List[str]:
        counts = Counter(words[0])
        for word in words[1:]:
            count = Counter(word)
            delete = []
            for ch, fr in counts.items():
                if ch not in count:
                    delete.append(ch)
                else:
                    counts[ch] = min(count[ch], fr)
            for ch in delete:
                del counts[ch]
        res = []
        for ch, fr in counts.items():
            if fr == 1:
                res.append(ch)
            else:
                res.extend([ch] * fr)
        return res