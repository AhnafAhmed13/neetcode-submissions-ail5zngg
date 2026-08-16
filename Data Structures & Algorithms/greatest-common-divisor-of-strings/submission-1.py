class Solution:
    import math
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""
        if str1 == str2:
            return str1

        s1, s2 = str1, str2
        if len(str2) > len(str1):
            s1, s2 = str2, str1

        res = ""
        start = s1[0]
        i = 0
        while i < len(s2):
            if s2[i] == start:
                j = i + 1
                while j < len(s2) and s2[j] == s1[j]:
                    j += 1
                    curr_len = j - i
                    if len(s1) % curr_len == 0 and\
                    len(s2) % curr_len == 0:
                        t1 = len(s1) // curr_len
                        t2 = len(s2) // curr_len
                        curr = s2[i:j]
                        if curr * t1 == s1 and curr * t2 == s2:
                            if len(curr) > len(res):
                                res = curr
                i = j
            else:
                i += 1
        return res
                        