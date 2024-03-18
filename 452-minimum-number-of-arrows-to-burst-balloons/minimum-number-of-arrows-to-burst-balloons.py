class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda point: point[0])

        prev = points[0]
        count = 1

        for i in range(1, len(points)):
            curr_start = points[i][0]
            curr_end = points[i][1]
            prev_start = prev[0]
            prev_end = prev[1]

            # Overlapping case
            if curr_start > prev_end: 
                count += 1
                prev = points[i]
            else:
                # Defining the overlapped region
                prev[0] = max(curr_start, prev_start)
                prev[1] = min(curr_end, prev_end)
        return count