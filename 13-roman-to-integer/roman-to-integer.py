class Solution:
    def romanToInt(self, s: str) -> int:
        hmap = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }

        num = 0

        for i in range(len(s) - 1):
            num += hmap[s[i]] if hmap[s[i]] >= hmap[s[i + 1]] else -hmap[s[i]]

        num += hmap[s[-1]]
            
        return num