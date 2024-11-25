class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter

        if not s and not t:
            return ""

        windowCount = {}
        countT = Counter(t)
        formed = 0
        required = len(countT)
        min_win_length = float("inf")
        min_win_idx = 0
        left, right = 0, 0

        # Expand the window by moving the right pointer
        while right < len(s):
            char = s[right]
            windowCount[char] = windowCount.get(char, 0) + 1

            if char in countT and windowCount[char] == countT[char]:
                formed += 1

            # Shrinking the window by moving the left pointer until the window is Invalid.
            while left <= right and formed == required:
                char = s[left] 

                # Calculate the min_window_length and min_wind_start_idx
                if right - left + 1 < min_win_length:
                    min_win_length = right - left + 1
                    min_win_idx = left

                # Shrink the window
                windowCount[char] -= 1

                # if the freq of char in window is less than char frequency in countT the formed -= 1 
                if char in countT and windowCount[char] < countT[char]:
                    formed -= 1

                left += 1

            right += 1
        
        return s[min_win_idx: min_win_idx + min_win_length] if min_win_length != float("inf") else ""