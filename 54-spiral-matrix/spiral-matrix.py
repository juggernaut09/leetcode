class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left = 0 
        right = len(matrix[0]) - 1
        top = 0
        bottom = len(matrix) - 1
        res = []

        while left <= right and top <= bottom:
            # Traverse from left to right along the same row
            for i in range(left, right + 1):
                res.append(matrix[top][i])

            top += 1

            # traverse from top to bottom along the same col
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
    
            right -= 1

            if top <= bottom:
                # traverse from right to left along the same row
                for i in range(right, left - 1, -1):
                    res.append(matrix[bottom][i])

                bottom -= 1

            if left <= right:
                # traverse from bottom to top along the same col
                for i in range(bottom, top - 1, -1):
                    res.append(matrix[i][left])

                left += 1

        return res