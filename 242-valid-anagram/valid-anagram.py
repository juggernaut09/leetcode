class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter_s = Counter(s)
        counter_t = Counter(t)
        if sum(counter_s.values()) != sum(counter_t.values()):
            return False
        for char in counter_s.keys():
            if counter_s[char] != counter_t[char]: 
                return False
                
        return True