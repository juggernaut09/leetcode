class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(' ')
        if len(pattern) != len(s):
            return False
        
        hmap = {}
        used_words = set()


        for i in range(len(pattern)):
            if pattern[i] not in hmap.keys():
                if s[i] in used_words:
                    return False
                hmap[pattern[i]] = s[i]
                used_words.add(s[i])
            else: 
                if hmap[pattern[i]] != s[i]:
                    return False
        return True