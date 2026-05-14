class Solution(object):
    def topStudents(self, positive_feedback, negative_feedback, report, student_id, k):
        """
        :type positive_feedback: List[str]
        :type negative_feedback: List[str]
        :type report: List[str]
        :type student_id: List[int]
        :type k: int
        :rtype: List[int]
        """
        neg = set(negative_feedback)
        pos = set(positive_feedback)

        scores = {}
        for r, sid in zip(report, student_id):
            # initialize every student 0, 
            scores[sid] = scores.get(sid, 0)
            for word in r.split():
                if word in pos:
                    scores[sid] += 3
                if word in neg:
                    scores[sid] -= 1
        sorted_student = sorted(scores.items(), key=lambda x: (-x[1], x[0]))
        return [sid for sid, scores in sorted_student[:k]]
        