class Solution:
    def hammingWeight(self, n: int) -> int:
        from collections import Counter
        return Counter(bin(n)[2:])['1']

