class Solution:
    def firstUniqChar(self, s: str) -> int:
        countS = {}
        for i in range(len(s)):
            if s[i] in countS.keys():
                countS[s[i]] = -1
            else:
                countS[s[i]] = i

        for key, value in countS.items():
            if value >= 0:
                return value
        return -1  
        