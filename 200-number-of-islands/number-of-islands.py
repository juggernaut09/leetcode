class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #### dfs ####
        # def dfs(row, col):
        #     if row >= len(grid) or row < 0 or col >= len(grid[0]) or col < 0 or grid[row][col] != "1":
        #         return -1
        #     grid[row][col] = "0"
        #     # left
        #     dfs(row, col - 1)

        #     # right
        #     dfs(row, col + 1)

        #     # up
        #     dfs(row - 1, col)

        #     # down
        #     dfs(row + 1, col)

        # num_of_islands = 0

        # for row in range(len(grid)):
        #     for col in range(len(grid[0])):
        #         if grid[row][col] == "1":
        #             dfs(row, col)
        #             num_of_islands += 1

        # return num_of_islands

        #### BFS ####
        def bfs(row, col):
            queue = [[row, col]]
            grid[row][col] == "0"

            while queue:
                r, c = queue.pop(0)

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == "1":
                        queue.append([nr, nc])
                        grid[nr][nc] = "0"

        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        num_of_islands = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    bfs(row, col)
                    num_of_islands += 1

        return num_of_islands