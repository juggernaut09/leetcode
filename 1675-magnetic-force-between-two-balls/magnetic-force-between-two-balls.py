class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        def can_place_balls(position, m, force):
            count, prev = 1, position[0]
            for pos in position[1:]:
                if pos - prev >= force:
                    count += 1
                    prev = pos
                if count == m:
                    return True
            return False

        position.sort()
        low, high = 1, position[-1] - position[0]
        res = 0

        while low <= high:
            mid = (low + high) // 2
            if can_place_balls(position, m, mid):
                res = mid
                low = mid + 1
            else:
                high = mid - 1

        return res