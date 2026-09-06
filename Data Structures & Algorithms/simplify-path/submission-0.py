class Solution:
    def simplifyPath(self, path: str) -> str:
        parts = path.split("/"); res = []
        for p in parts:
            if p == "." or p == "": continue
            elif p == "..":
                if len(res) > 0: res.pop()
                else: continue
            else: res.append(p)
        return "/" + "/".join(res)