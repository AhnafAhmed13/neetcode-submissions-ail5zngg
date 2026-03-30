class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        mapping = {
            "0": "0",
            "1": "1",
            "2": "5",
            "5": "2",
            "6": "9",
            "8": "8",
            "9": "6"
        }
        s = []
        for d in num:
            if d not in mapping:
                return False
            s.append(mapping[d])
        return num == "".join(s[::-1])