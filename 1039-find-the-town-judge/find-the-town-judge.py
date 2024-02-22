class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1 and len(trust) == 0:
            return 1
        
        hmap = {}
        for (i, j) in trust:
            if not i in hmap:
                hmap[i] = -1
            else:
                hmap[i] -= 1

            hmap[j] = hmap.get(j, 0) + 1
            
        for key, value in hmap.items():
            if value == n-1:
                return key

        return -1            
