class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(' ')
        if len(pattern) != len(s):
            return False
        
        hmap = {}
        
        for p, word in zip(pattern, s):
            if p in hmap.keys():
                if hmap[p] != word:
                    return False
            else:
                if word in hmap.values():
                    return False
                hmap[p] = word
        
        return True