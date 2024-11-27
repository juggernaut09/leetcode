class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        left, right = 0, 0

        max_len = 0
        charSet = set()

        # Expand the window
        while right < len(s):

            # Shrinking the window 
            while s[right] in charSet:
                left_char = s[left]
                charSet.remove(left_char)
                left += 1 
            
            charSet.add(s[right])
            max_len = max(max_len, right - left + 1)
            right += 1 
            
        return max_len