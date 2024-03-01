class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        res = '0'*len(s)
        res = list(res)
        j = 0
        for c in s:
            if c == '1':
                if res[len(res) - 1] != '1':
                    res[len(res) - 1] = c
                else:
                    if res[j] != '1':
                        res[j] = c
                        j += 1
            else:
                continue
        return ''.join(res)

        