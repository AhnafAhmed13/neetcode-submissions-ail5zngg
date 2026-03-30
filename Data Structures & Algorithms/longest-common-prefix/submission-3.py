class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        '''
        I - strs: list[str]
        O - str
        C - N/A
        E - no longest common prefix -> ""

        Plan: iterate over the list and check if a str is has common prefix with
        current longest common prefix, if yes set current as minimum of the 2
        if no, return ""

        Steps:

        curr = first str
        for s in strs:
            n = len(s)
            if len(s) > len(curr):
                n = len(curr)
            for i in range(n):
                if s[i] != curr[i]:
                    if i == 0:
                        return ""
                    else:
                        curr = curr[:i]
        return curr
        '''


        curr = strs[0]
        for s in strs:
            if s == "":
                return ""
                
            if len(s) < len(curr):
                curr = curr[:len(s)]
                
            for i in range(len(curr)):
                if s[i] != curr[i]:
                    if i == 0:
                        return ""
                    else:
                        curr = curr[:i]
                        break
        return curr