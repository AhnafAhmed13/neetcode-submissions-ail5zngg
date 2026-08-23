class Solution:
    from collections import defaultdict
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        users = defaultdict(list) # { u : [(t, w), ...] }
        for i in range(len(username)):
            users[username[i]].append((timestamp[i], website[i]))

        scores = defaultdict(int)
        for v in users.values():
            if len(v) >= 3:
                # sort by time (just in case)
                v.sort(key=lambda x: x[0])
                curr = set()
                for i in range(len(v)):
                    for j in range(i + 1, len(v)):
                        for k in range(j + 1, len(v)):
                            curr.add((v[i][1], v[j][1], v[k][1]))
                for t in curr:
                    scores[t] += 1
        # print(scores)
        scores = sorted(list(scores.items()), key=lambda x: (-x[1], x[0]))
        # print(scores)
        return list(scores[0][0])



        