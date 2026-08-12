class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) == 1:
            return 1
            
        k = 1
        curr_len = 1
        for i in range(1, len(chars)):
            if chars[i - 1] != chars[i]:
                if curr_len > 1:
                    for d in str(curr_len):
                        chars[k] = d
                        k += 1
                chars[k] = chars[i]
                k += 1
                curr_len = 1
            else:
                curr_len += 1
        
        if curr_len > 1:
            for d in str(curr_len):
                chars[k] = d
                k += 1

        return k