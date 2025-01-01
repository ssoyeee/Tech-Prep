class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        # [2, 2, 3]
        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(candidates) or total > target:
                return
            # first decision
            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])
            cur.pop() #can't include current in the future, so before call the next dfs pop it
            dfs(i+1, cur, total)

        dfs(0, [], 0)
        return res