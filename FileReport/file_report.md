
# File System Report Generator

Imagine we have a system that stores files, and these files can be grouped into collections. We are interested in knowing where our resources are being taken up. 

For this system, we would like to generate a report that lists:
- The **total size of all files stored**.
- The **top N collections (by file size)**, where `N` can be a user-defined value.

## Example Input
- file1.txt (size: 100)
- file2.txt (size: 200) in collection “collection1”
- file3.txt (size: 200) in collection “collection1”
- file4.txt (size: 300) in collection “collection2”
- file5.txt (size: 10)

### Explanation of Input

- **Files**: Each file has a name and a size.
- **Collections**: Files can optionally belong to one or more collections (e.g., "collection1").
- **Files Without Collections**: Some files may not belong to any collection.

## Expected Output

### Total Size of All Files
- 810

### File Sizes by Collection
- `"collection1"`: 2 files, total size `400`
- `"collection2"`: 1 file, total size `300`
- Files without any collection: 2 files, total size `110`

### Example: Top N Collections
If `N = 2`, the top 2 collections would be:
- [“collection1”, “collection2”]

### Top Collections Logic
The **top N collections** are determined by the total size of all files associated with each collection, sorted in descending order of size. Collections with larger total file sizes appear at the top.