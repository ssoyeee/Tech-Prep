class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        def dfs(index):
            visited[index] = True
            for i in range(n):
                if not visited[i] and graph[index][i]:
                    dfs(i)
            
       # Input and initialize
        graph = [[False] * n for _ in range(n)]
        visited = [False] * n
        answer = 0
        
        # fill out connected components
        for u, v in edges:
            graph[u][v] = True
            graph[v][u] = True
        
        # call dfs
        for i in range(n):
            if not visited[i]:
                dfs(i)
                answer += 1  

        return answer