class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []; N = len(words); i = 0
        while i < N:
            curr = [words[i]]; remaining = maxWidth - len(words[i]); i += 1
            while i < N and len(words[i]) + 1 <= remaining:
                curr.append(" "); curr.append(words[i])
                remaining -= (len(words[i]) + 1); i += 1
            if remaining > 0:
                num_words = len(curr)
                if num_words > 1:
                    num_words = num_words // 2 + 1
                    space = remaining // (num_words - 1)
                    extra = remaining % (num_words - 1)
                    for j in range(1, len(curr), 2):
                        if extra > 0:
                            curr[j] += " " * (space + 1)
                            extra -= 1
                        else: curr[j] += " " * space
                else:
                    curr.append(" " * remaining)
            res.append(curr)

        for i in range(len(res) - 1):
            res[i] = "".join(res[i])
        space = 0
        for i in range(1, len(res[-1]), 2):
            space += len(res[-1][i]) - 1
            res[-1][i] = " "
        res[-1][-1] += " " * space
        res[-1] = "".join(res[-1])
        return res

