class Solution:
    def makeGood(self, s: str) -> str:
        if not len(s):
            return s

        res = []
        res.append(s[0])

        for i in range(1, len(s)):
            if not len(res):
                res.append(s[i])
            else:
                if (ord(res[-1]) == ord(s[i]) - 32) or (ord(res[-1]) == ord(s[i]) + 32):
                    res.pop()
                else:
                    res.append(s[i])
        return ''.join(res)

        
