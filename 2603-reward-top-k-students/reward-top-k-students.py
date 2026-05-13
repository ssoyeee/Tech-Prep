class Solution:
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
        # Build lookup sets for O(1) word check
        pos = set(positive_feedback)
        neg = set(negative_feedback)
        # Calculate score for each student
        scores = {}
        for r, sid in zip(report, student_id):
            # Initialize score to 0 if student not yet in scores
            scores[sid] = scores.get(sid, 0) 
            for word in r.split():
                if word in pos:
                    scores[sid] += 3
                if word in neg:
                    scores[sid] -= 1
        # Sort by score desc, then by student_id asc 
        sorted_students = sorted(scores.items(), key=lambda x: (-x[1], x[0]))

        # return top k student_ids
        return [sid for sid, scores in sorted_students[:k]]

        # T: O(N log N) ---- O(W+R*L+NlogN) where W=pos/neg set, R*L= iterating over reports*avg words per report, NlogN for sorting
        # S: O(N) ---- O(W+N) where N= scores dict, W= pos/neg set