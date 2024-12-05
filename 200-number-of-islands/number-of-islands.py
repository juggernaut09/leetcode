class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(row, col):
            if not 0 <= row < len(grid) or not 0 <= col < len(grid[0]) or grid[row][col] != "1":
                return - 1
                
            grid[row][col] = "0"
            dfs(row - 1, col)
            dfs(row + 1, col)
            dfs(row, col - 1)
            dfs(row, col + 1)

        num_of_islands = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    dfs(row, col)
                    num_of_islands += 1


        return num_of_islands