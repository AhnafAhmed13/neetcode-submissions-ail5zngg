class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False

        from collections import defaultdict
        hashmap = defaultdict(set)
        for a, b in similarPairs:
            hashmap[a].add(b)
            hashmap[b].add(a)

        for i in range(len(sentence1)):
            a, b = sentence1[i], sentence2[i]
            if a == b:
                continue
            elif a in hashmap and b in hashmap[a]:
                continue
            elif b in hashmap and a in hashmap[b]:
                continue
            else:
                return False
        
        return True