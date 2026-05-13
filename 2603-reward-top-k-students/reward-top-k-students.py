class Solution:
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
        pos = set(positive_feedback)
        neg = set(negative_feedback)
        scores = {}
        for r, sid in zip(report, student_id):
            scores[sid] = scores.get(sid, 0)
            for word in r.split():
                if word in pos:
                    scores[sid] += 3
                if word in neg:
                    scores[sid] -= 1
        sorted_students = sorted(scores.items(), key=lambda x: (-x[1], x[0]))
        return [sid for sid, scores in sorted_students[:k]]