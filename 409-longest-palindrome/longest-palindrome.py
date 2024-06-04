class Solution:
    def longestPalindrome(self, s: str) -> int:
        hmap = {}
        odd_freq = 0
        for c in s:
            if c not in hmap.keys():
                hmap[c] = 1
                odd_freq += 1
            else:
                hmap[c] += 1
                if hmap[c] % 2 == 0:
                    odd_freq -= 1
                else:
                    odd_freq += 1

        return len(s) - odd_freq + (odd_freq != 0)
