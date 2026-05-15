class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        visited = set()

        def dfs(i):
            if i >= len(arr) or i < 0:
                return False
            if arr[i] == 0:
                return True
            if i in visited:
                return False
            visited.add(i)
            return dfs(i+arr[i]) or dfs(i-arr[i])
        return dfs(start)

    #T: O(N) where N is len(arr)
    #S: O(N) for visited set