class Solution:
    def applySubstitutions(self, replacements: List[List[str]], text: str) -> str:
        r = {f'%{k}%': v for k, v in replacements}
        while True:
            c = 0
            for k in r:
                if k in text:
                    text = text.replace(k, r[k])
                    c += 1
            if c == 0:
                return text


            