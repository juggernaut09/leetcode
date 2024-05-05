class Solution:
    def numRescueBoats(self, p: List[int], limit: int) -> int:
        p.sort()
        i, j = 0, len(p) - 1
        boats = 0

        while i <= j:
            if i == j:
                boats += 1
                return boats
                
            if p[i] + p[j] <= limit:
                i += 1
                j -= 1
                boats += 1
            else:
                j -= 1
                boats += 1

        return boats
        