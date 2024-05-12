class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        maxLocal = [[0] * (n - 2) for _ in range(n - 2)] 
        for row in range(len(maxLocal)):
            for col in range(len(maxLocal[0])):
                res = -1
                for i in range(row, row + 3):
                    for j in range(col, col + 3):
                        res = max(res, grid[i][j])
                        print(i, j, res)
                maxLocal[row][col] = res
                # print("row : {}, col: {} = {}".format(row, col, res))
                # print(maxLocal[row][col])
            # print(" ---> row : {}, col: {} = {}".format(0, 0, maxLocal[0][0]))
            # print(" ---> row : {}, col: {} = {}".format(0, 1, maxLocal[0][1]))
        return maxLocal 