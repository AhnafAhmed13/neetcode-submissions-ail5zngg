class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        ops = 0; cls = 0; res = []
        for i in range(len(s)):
            if s[i] == "(":
                ops += 1
            if s[i] == ")":
                if cls == ops:
                    continue
                else:
                    cls += 1
            res.append(s[i])
        if ops > cls:
            k = ops - cls; i = len(res) - 1
            while k > 0 and i >= 0:
                if res[i] == "(":
                    res[i] = ""
                    k -= 1
                i -= 1
        return "".join(res)