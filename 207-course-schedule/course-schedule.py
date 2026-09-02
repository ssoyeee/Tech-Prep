class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = defaultdict(list)
        for course, prereq in prerequisites:
            graph[course].append(prereq)
        visiting = set()
        visited = set()

        def dfs(node):
            if node in visiting:
                return False
            if node in visited:
                return True
            visiting.add(node)

            for prereq in graph[node]:
                if not dfs(prereq):
                    return False
            visiting.remove(node)
            visited.add(node)
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True