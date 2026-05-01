class Solution:
    def frequencySort(self, s: str) -> str:
        counts = Counter(s)
        sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
        
        return "".join(val * freq for val, freq in sorted_counts)

        # T: O(N log N) where N = unique characters
        # S: O(N)
            