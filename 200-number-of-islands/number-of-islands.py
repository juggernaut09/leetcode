class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i: int, j: int) -> None:
            if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] == "0":
                return

            if grid[i][j] == "$":
                return
                
            grid[i][j] = "$"
            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)
            return

        rows = len(grid)
        cols = len(grid[0])
        islands = 0    
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    dfs(i, j)
                    islands += 1
        
        return islands
        