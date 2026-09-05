class WordDistance:
    from collections import defaultdict
    def __init__(self, wordsDict: List[str]):
        self.words = wordsDict
        self.words_dict = defaultdict(list)
        for i, w in enumerate(wordsDict):
            self.words_dict[w].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        w1_idxs = self.words_dict[word1]
        w2_idxs = self.words_dict[word2]
        res = abs(w1_idxs[0] - w2_idxs[0])
        for idx1 in w1_idxs:
            for idx2 in w2_idxs:
                res = min(res, abs(idx1 - idx2))
        return res


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)
