class Solution:
    def customSortString(self, order: str, s: str) -> str:
        s_map = {}
        for c in s:
            s_map[c] = s_map.get(c, 0) + 1
        
        res = ""

        for c in order:
            if c in s_map.keys():
                res = res + c * s_map[c]
                del s_map[c]

        for key, value in s_map.items():
            res = res + key * value
        return res


        
