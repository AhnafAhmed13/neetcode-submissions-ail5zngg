class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        '''
        I - strs: list[str]
        O - str
        C - N/A
        E - no longest common prefix -> ""
            if a str is "" -> ""

        Plan: iterate over the list and check if a str is has common prefix with
        current longest common prefix, if yes set current as minimum of the 2
        if no, return ""

        Steps:

        initialize longest as first str in the list

        for each str
            check if str is empty, return ""
            check if str is shorter than current longest
                update longest by trimming to current str's length
            for each char in str
                compare with longest
                if different
                    if the first char is different, return ""
                    otw, update longest by trimming to matching char's position
                    stop comparing current str
                    
        return longest


        '''

        longest = strs[0]

        for curr in strs:

            # Edge case
            if curr == "":
                return ""
                
            # Trim longest
            if len(curr) < len(longest):
                longest = longest[:len(curr)]

            # Compare each char
            for i in range(len(longest)):
                if curr[i] != longest[i]:
                    if i == 0: # No match
                        return ""
                    else: # Trim longest
                        longest = longest[:i]
                        break

        return longest