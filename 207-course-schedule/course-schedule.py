class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True
        
        graph = collections.defaultdict(list)
        indegrees = [0] * numCourses
        
        for prerequisite in prerequisites:
            graph[prerequisite[1]].append(prerequisite[0])
            indegrees[prerequisite[0]] += 1

        queue = deque(i for i in range(numCourses) if indegrees[i] == 0)      
        completedCourses = 0    
        while queue:
            node = queue.popleft()
            for dependent_node in graph[node]:
                indegrees[dependent_node] -= 1
                if indegrees[dependent_node] == 0:
                    queue.append(dependent_node)
            
            completedCourses += 1

        return numCourses == completedCourses

    # Topological Sort by BFS
    # Time: O(V+E)
    # Space: O(V+E)