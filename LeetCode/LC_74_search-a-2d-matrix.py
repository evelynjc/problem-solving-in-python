class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        merged_list = []
        # merge the given list into one
        for i in matrix:
            merged_list += i
        # find targget in the merged list
        return target in merged_list