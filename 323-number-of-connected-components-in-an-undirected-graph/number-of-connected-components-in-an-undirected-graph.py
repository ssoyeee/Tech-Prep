class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # union find
        parent = [i for i in range(n)]
        rank = [1] * n

        def find(n1):
            result = n1

            while result != parent[result]:
                parent[result] = parent[parent[result]]
                result = parent[result]
            return result
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return 0
            
            if rank[p2]> rank[p1]:
                parent[p1] = p2
                rank[p2] += rank[p1]
            else:
                parent[p2] = p1
                rank[p1] += rank[p2]
            return 1

        result = n
        for n1, n2 in edges:
            result -= union(n1, n2)
        return result

        '''
        # dfs
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
        T: O(E+V)
        S: O(E+V)
        '''