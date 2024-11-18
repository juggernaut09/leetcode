class Solution:
    def countBits(self, n: int) -> List[int]:
        from collections import Counter
        res = []
        for i in range(n+1):
            res.append(Counter(bin(i)[2:])['1'])
        return res
