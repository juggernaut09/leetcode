class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        exptected = sorted(heights)
        count = 0
        for i in range(len(heights)):
            count += (exptected[i] != heights[i])
        return count