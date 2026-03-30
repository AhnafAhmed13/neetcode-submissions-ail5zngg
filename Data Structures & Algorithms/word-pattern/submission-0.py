class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False
        l2w = {}
        w2l = {}
        for i in range(len(pattern)):
            l = pattern[i]
            w = words[i]
            if l in l2w:
                if w != l2w[l]:
                    return False
            else:
                l2w[l] = w
            if w in w2l:
                if l != w2l[w]:
                    return False
            else:
                w2l[w] = l
        return True