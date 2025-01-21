import heapq
from collections import defaultdict

class File:
    def __init__(self, size, file_name, collections=None):
        self.size = size
        self.file_name = file_name
        self.collections = collections if collections else []

class Report:
    def __init__(self, total_size, collections):
        self.total_size = total_size
        self.collections = collections

    def __str__(self):
        return f"-- Report --\nTotal Size: {self.total_size} KB\nTop K Collections: {self.collections}"

class FileReport:
    def generate_report(self, files, k):
        total_size = 0
        collection_sizes = defaultdict(int)

        # Calculate total file size and collection sizes
        for file in files:
            total_size += file.size
            for collection in file.collections:
                collection_sizes[collection] += file.size

        # Use a min-heap to get the top K largest collections
        min_heap = []
        for collection, size in collection_sizes.items():
            heapq.heappush(min_heap, (size, collection))
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        # Extract top K collections from the heap and reverse for largest-to-smallest order
        top_k_collections = [heapq.heappop(min_heap)[1] for _ in range(len(min_heap))]
        top_k_collections.reverse()

        return Report(total_size, top_k_collections)

# Example Usage
if __name__ == "__main__":
    f1 = File(200, "file1.txt")
    f2 = File(100, "file2.txt", ["collection1", "collection2"])
    f3 = File(50, "file3.txt", ["collection1", "collection3"])
    f4 = File(10, "file4.txt", ["collection1", "collection2", "collection3"])
    f5 = File(1000, "file5.txt", ["collection4"])

    files = [f1, f2, f3, f4, f5]

    fr = FileReport()
    report = fr.generate_report(files, 2)
    print(report)

'''
Expected output:
    -- Report --
Total Size: 1360 KB
Top K Collections: ['collection4', 'collection1']
'''
# Time: O(N+M+U*logK+K*logK)
# Space: O(U+K)