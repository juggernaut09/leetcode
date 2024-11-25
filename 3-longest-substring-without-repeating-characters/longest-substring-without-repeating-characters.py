class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        charSet = set()
        max_length = 0
        left = 0

        for right in range(n):
            if s[right] not in charSet:
                charSet.add(s[right])
                max_length = max(max_length, right - left + 1)
            else:
                while s[right] in charSet:
                    charSet.remove(s[left])
                    left += 1
                charSet.add(s[right])
        return max_length