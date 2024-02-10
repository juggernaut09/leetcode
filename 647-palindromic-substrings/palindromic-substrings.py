class Solution:
    def countPalindrome(self, s: str, l: int, r: int) -> int:
        res = 0
        while l>=0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
        return res

    def countSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            l=r=i
            # Count odd palindrome strings.
            res += self.countPalindrome(s, l, r)

            #  Count even Palindrome Strings.
            l = i
            r = l+1
            res += self.countPalindrome(s, l, r)
        return res 
