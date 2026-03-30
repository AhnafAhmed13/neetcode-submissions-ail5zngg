class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        if abbr.isnumeric() and int(abbr) == len(word):
            return True
        
        i = j = 0
        while i < len(word) and j < len(abbr):
            if abbr[j].isdigit():
                jump = abbr[j]
                if jump == '0':
                    return False

                j += 1
                while j < len(abbr) and abbr[j].isdigit():
                    jump += abbr[j]
                    j += 1

                i += int(jump)

            else:
                if word[i] != abbr[j]:
                    return False
                i += 1
                j += 1
                
        return i == len(word) and j == len(abbr)