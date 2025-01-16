class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # 0. initialize
        graph = defaultdict(list)
        indegrees = [0] * numCourses

        for prerequisite in prerequisites:
            graph[prerequisite[1]].append(prerequisite[0])
            indegrees[prerequisite[0]] += 1
        
        queue = deque(i for i in range(numCourses) if indegrees[i] == 0)
        index = 0
        order = [0] * numCourses
        while queue:
            course = queue.popleft()
            for dependent_course in graph[course]:
                indegrees[dependent_course] -= 1
                if indegrees[dependent_course] == 0:
                    queue.append(dependent_course)
            order[index] += course
            index += 1
        return order if index == numCourses else []
        