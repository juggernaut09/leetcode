class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(row, col):
            if row >= len(grid) or row < 0 or col >= len(grid[0]) or col < 0 or grid[row][col] != "1":
                return -1
            grid[row][col] = "0"
            # left
            dfs(row, col - 1)

            # right
            dfs(row, col + 1)

            # up
            dfs(row - 1, col)

            # down
            dfs(row + 1, col)

        num_of_islands = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    dfs(row, col)
                    num_of_islands += 1

        return num_of_islands