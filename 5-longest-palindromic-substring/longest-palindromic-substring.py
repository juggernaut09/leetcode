class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.max_str = ""
        for i in range(len(s)):
            s1 = self.helper(s, i, i)
            s2 = self.helper(s, i, i + 1)
        return s2

    def helper(self, s: str, left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if len(self.max_str) < (right - left + 1):
                    self.max_str = s[left : right + 1]

                left -= 1
                right += 1
            return self.max_str    
