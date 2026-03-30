class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        from collections import defaultdict
        d = defaultdict(list)
        for s in strings:
            # print(s)
            key = []
            for i in range(len(s) - 1):
                tmp = (chr((ord(s[i + 1]) - ord(s[i])) % 26 + ord('a')))
                key.append(tmp)
            # print(key)
            d[''.join(key)].append(s)
        return list(d.values())