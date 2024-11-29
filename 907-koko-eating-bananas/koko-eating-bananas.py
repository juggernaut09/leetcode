class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can_eat_all(k):
            total_no_hrs = 0

            for pile in piles:
                total_no_hrs += (pile + k - 1) // k

            return total_no_hrs <= h


        left, right = 1, max(piles)

        while left < right:
            mid = (left + right) // 2

            if can_eat_all(mid):
                right = mid
            else:
                left = mid + 1

        return left

