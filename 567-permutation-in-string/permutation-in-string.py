class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        if len(s1) < len(s2):
            small_str = s1
            large_str = s2
        else:
            small_str = s2
            large_str = s1
        
        w_size = len(small_str)
        l, r = 0, w_size
        while(r <= len(large_str)):
            if sorted(small_str) == sorted(large_str[l:r]):
                return True 
            l += 1
            r += 1
        return False