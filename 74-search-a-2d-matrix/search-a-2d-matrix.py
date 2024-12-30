class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # Row wise binary search
        top = 0
        bottom = len(matrix) - 1

        while top <= bottom:
            row = (top + bottom) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bottom = row - 1
            else:
                break
        
        if not (top <= bottom):
            return False
        
        # col wise binary search
        row = (top + bottom) // 2

        l = 0
        r = len(matrix[row]) - 1

        while l <= r:
            mid = (l + r) // 2
            if target > matrix[row][mid]:
                l = mid + 1
            elif target < matrix[row][mid]:
                r = mid - 1
            else:
                return True

        return False

        