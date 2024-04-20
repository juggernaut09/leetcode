class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        

        def dfs(i: int, j: int) -> (int, int):
            if i < 0 or j < 0 or i >= rows or j >= cols or land[i][j] == 0:
                return (i - 1, j - 1)
            
            land[i][j] = 0
            curr_row, curr_col = i, j
            
            r, c = dfs(i - 1, j)
            curr_row = max(curr_row, r)
            curr_col = max(curr_col, c)
            
            r, c = dfs(i + 1, j)
            curr_row = max(curr_row, r)
            curr_col = max(curr_col, c)

            r, c = dfs(i , j - 1)
            curr_row = max(curr_row, r)
            curr_col = max(curr_col, c)

            r, c = dfs(i, j + 1)
            curr_row = max(curr_row, r)
            curr_col = max(curr_col, c)

            return (curr_row, curr_col)


        rows = len(land)
        cols = len(land[0])
        res = []
        for i in range(rows):
            for j in range(cols):
                arr = []
                if land[i][j]:
                    arr.append(i)
                    arr.append(j)
                    b_row, b_col = dfs(i, j)
                    arr.append(b_row)
                    arr.append(b_col)
                    res.append(arr)
        return res
