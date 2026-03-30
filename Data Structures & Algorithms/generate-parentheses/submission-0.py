class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []

        def generator(s, o, c):

            if o == 0 and c == 0:
                res.append(s)

            if o <= c:
                if o > 0:
                    generator(s + "(", o - 1, c)
                
                if c > 0:
                    generator(s + ")", o, c - 1)


        generator("", n, n)

        return res