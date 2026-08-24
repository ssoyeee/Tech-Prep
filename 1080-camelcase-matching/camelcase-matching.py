class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        def match(query, pattern):
            # two pointer
            j = 0
            for ch in query:
                if j < len(pattern) and ch == pattern[j]:
                    j+=1
                elif ch.isupper():
                    return False
            return j == len(pattern)
        return [match(q, pattern) for q in queries]