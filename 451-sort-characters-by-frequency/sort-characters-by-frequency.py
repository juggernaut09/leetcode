class Solution:
    def frequencySort(self, s: str) -> str:
        hmap = {}
        for c in s:
            hmap[c] = hmap.get(c, 0) + 1
        
        sorted_hmap = dict(sorted(hmap.items(), key = lambda x: x[1],  reverse=True))

        res = []
        for key, value in sorted_hmap.items():
            res.append(key * value)

        return ''.join(r for r in res)

        