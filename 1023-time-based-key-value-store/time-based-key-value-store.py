class TimeMap:
    def __init__(self):
        self.key_time_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        # Time O(1), Space O(K*N)
        self.key_time_map[key].append((timestamp, value))
        
    def get(self, key: str, timestamp: int) -> str:
        # Time O(logN), Space O(K*N) where K is number of key, N is number of value stored at each key
        if not key in self.key_time_map:
            return ""

        if timestamp < self.key_time_map[key][0][0]:
            return ""
                
        left = 0
        right = len(self.key_time_map[key]) - 1
                
        while left <= right:
            mid = (left + right) // 2
            if self.key_time_map[key][mid][0] <= timestamp:
                left = mid + 1
            else:
                right = mid - 1

        return "" if right < 0 else self.key_time_map[key][right][1]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)