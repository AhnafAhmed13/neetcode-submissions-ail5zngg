class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        
        def top_five_ave(scores):
            scores.sort(reverse=True)
            return sum(scores[:5]) // 5

        student_scores = {}

        for sid, scores in items:
            if sid not in student_scores:
                student_scores[sid] = []
            student_scores[sid].append(scores)

        res = []
        for sid, scores in student_scores.items():
            res.append([sid, top_five_ave(scores)])

        res.sort(key=lambda x: x[0])

        return res