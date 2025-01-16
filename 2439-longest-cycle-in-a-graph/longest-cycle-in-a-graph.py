class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        graph = defaultdict(list)
        indegrees = [0] * len(edges)

        for i in range(len(edges)):
            if edges[i] != -1: # if theres outgoing edge
                graph[i].append(edges[i])
                indegrees[edges[i]] += 1

        queue = deque(i for i in range(len(edges)) if indegrees[i] == 0)
        visited = [False] * len(edges)

        while queue:
            node = queue.popleft()
            for dependent_node in graph[node]:
                indegrees[dependent_node] -= 1
                if indegrees[dependent_node] == 0:
                    queue.append(dependent_node)
            visited[node] = True
        
        max_cycle = -1
        for i in range(len(edges)):
            if not visited[i]:
                cycle_length = self.calculate_cycle_length(edges, visited, i)
                max_cycle = max(max_cycle, cycle_length)
        return max_cycle

    def calculate_cycle_length(self, edges, visited, start_node):
        length = 1
        visited[start_node] = True
        dependent_node = edges[start_node]

        while dependent_node != start_node:
            visited[dependent_node] = True
            node = dependent_node
            dependent_node = edges[dependent_node]
            length += 1
        return length
    
    # Time: O(V+E)
    # Space: O(V+E)