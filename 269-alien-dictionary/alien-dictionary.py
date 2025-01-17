class Solution:
    def alienOrder(self, words: List[str]) -> str:
        
        n = len(words)
        graph = defaultdict(set)
        indegrees = {c: 0 for word in words for c in word}

        # Build the graph and compute indegrees
        for i in range(1, n):
            prev, curr = words[i - 1], words[i]
            if prev != curr and prev.startswith(curr):
                return ""
            
            for j in range(min(len(prev), len(curr))):
                if prev[j] != curr[j]:
                    if curr[j] not in graph[prev[j]]:
                        graph[prev[j]].add(curr[j])
                        indegrees[curr[j]] += 1
                    break

        # Perform topological sort using BFS
        queue = deque([c for c in indegrees if indegrees[c] == 0])
        result = []

        while queue:
            c = queue.popleft()
            result.append(c)

            for dependent_char in graph[c]:
                indegrees[dependent_char] -= 1
                if indegrees[dependent_char] == 0:
                    queue.append(dependent_char)

        return "".join(result) if len(result) == len(indegrees) else ""