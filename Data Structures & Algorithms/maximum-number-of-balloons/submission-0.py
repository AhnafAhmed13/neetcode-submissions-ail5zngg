class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        from collections import Counter
        c = Counter(text)
        if 'b' not in c: return 0
        b = c['b']
        if 'a' not in c: return 0
        a = c['a']
        if 'l' not in c: return 0
        l = c['l'] // 2
        if 'o' not in c: return 0
        o = c['o'] // 2
        if 'n' not in c: return 0
        n = c['n']
        return min(b, a, l, o, n)