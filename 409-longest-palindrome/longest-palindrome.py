class Solution:
    def longestPalindrome(self, s: str) -> int:
        st = set()
        res = 0
        for c in s:
            if c in st:
                res += 2
                st.remove(c)
            else:
                st.add(c)
        return res if not len(st) else res + 1