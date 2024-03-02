class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        count = 0
        for c in s:
            if c == '1':
                count += 1

        res = ['0'] * len(s)
        j = -1
        while count > 0:
            res[j] = '1'
            j += 1
            count -= 1
        
        return ''.join(res)

        
        