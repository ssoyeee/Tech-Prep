from typing import List, Dict
from collections import defaultdict

class File:
    def __init__(self, size: int, file_name: str, collections=None):
        self.size = size
        self.file_name = file_name
        self.collections = collections if collections else []

class Report:
    def __init__(self, total_size: int, collections: List[str]):
        self.total_size = total_size
        self.collections = collections

    def __str__(self):
        return f"-- Report --\nTotal Size: {self.total_size} KB\nTop K Collections: {self.collections}"

class FileReportQuickSelect:
    def generate_report(self, files: List[File], k: int) -> Report:
        total_size = 0
        collection_sizes = defaultdict(int)

        # Calculate total size and populate collection sizes
        for file in files:
            total_size += file.size
            for collection in file.collections:
                collection_sizes[collection] += file.size

        collections = list(collection_sizes.keys())
        n = len(collections)

        # Quickselect to find the top K largest collections
        k_index = n - k
        self.quickselect(collections, collection_sizes, 0, n - 1, k_index)

        top_k_collections = collections[k_index:]
        return Report(total_size, top_k_collections)

    def quickselect(self, collections: List[str], collection_sizes: Dict[str, int], left: int, right: int, k_index: int):
        if left < right:
            pivot_index = self.partition(collections, collection_sizes, left, right)
            if pivot_index == k_index:
                return
            elif pivot_index < k_index:
                self.quickselect(collections, collection_sizes, pivot_index + 1, right, k_index)
            else:
                self.quickselect(collections, collection_sizes, left, pivot_index - 1, k_index)

    def partition(self, collections: List[str], collection_sizes: Dict[str, int], start: int, pivot: int) -> int:
        pivot_value = collection_sizes[collections[pivot]]
        i = start
        for j in range(start, pivot):
            if collection_sizes[collections[j]] < pivot_value:
                collections[i], collections[j] = collections[j], collections[i]
                i += 1
        collections[i], collections[pivot] = collections[pivot], collections[i]
        return i

# Example Usage
if __name__ == "__main__":
    f1 = File(200, "file1.txt")
    f2 = File(100, "file2.txt", ["collection1", "collection2"])
    f3 = File(50, "file3.txt", ["collection1", "collection3"])
    f4 = File(10, "file4.txt", ["collection1", "collection2", "collection3"])
    f5 = File(1000, "file5.txt", ["collection4"])

    files = [f1, f2, f3, f4, f5]
    fr = FileReportQuickSelect()
    report = fr.generate_report(files, 2)
    print(report)

    # Total Time Complexity:  O(N + M + K)
    # Total Space Complexity:  O(M + log M)