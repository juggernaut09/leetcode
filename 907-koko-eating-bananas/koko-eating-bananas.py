class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = max(piles)

        while l <= r:
            k = (l + r) // 2

            total_hours = 0

            for p in piles:
                total_hours += math.ceil(p/k)
            
            if total_hours <= h:
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1

        return res

