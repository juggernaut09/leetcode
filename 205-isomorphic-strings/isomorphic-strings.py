class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        smap, tmap = {}, {}

        for i in range(len(s)):
            if s[i] in smap.keys():
                if smap[s[i]] != t[i]:
                    return False
            else:
                smap[s[i]] = t[i]
            
            if t[i] in tmap.keys():
                if tmap[t[i]] != s[i]:
                    return False
            else:
                tmap[t[i]] = s[i]


        return True

