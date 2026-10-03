class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        chars = set(list(source))
        res = 0
        while target:
            curr = 0; i = 0
            while curr < len(target) and i < len(source):
                if target[curr] not in chars: return -1
                if target[curr] == source[i]:
                    curr += 1
                i += 1
            target = target[curr:]
            res += 1
        return res
