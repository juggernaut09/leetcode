class Solution:
    def countBits(self, n: int) -> List[int]:
        from collections import Counter
        res = []
        for i in range(n+1):
            count = 0
            while i:
                count += i % 2
                i = i >> 1
            res.append(count)
        return res
