class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(s, l, r):
            while l<=r:
                if s[l] == s[r]:
                    l += 1
                    r -= 1
                else:
                    return False
            return True

        left = 0
        right = len(s) - 1
        while left <= right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return is_palindrome(s, left + 1, right) or is_palindrome(s, left, right - 1)

        return True