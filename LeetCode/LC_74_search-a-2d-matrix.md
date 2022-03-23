# 74. Search a 2D Matrix
https://leetcode.com/problems/search-a-2d-matrix/
```python
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        merged_list = []
        # merge the given list into one
        for i in matrix:
            merged_list += i
        # find targget in the merged list
        return target in merged_list
```
**Success**\
Runtime: 66 ms, faster than 45.15% of Python3 online submissions for Search a 2D Matrix.\
Memory Usage: 14.4 MB, less than 51.97% of Python3 online submissions for Search a 2D Matrix.