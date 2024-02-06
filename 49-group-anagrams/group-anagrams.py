class Solution:
    def get_hash(self, s: str) -> str:
        char_set = [0] * 26
        for c in s:
            char_set[ord(c) - ord('a')] += 1
        
        res = []
        for i in range(len(char_set)):
            if char_set[i] !=0:    
                res.extend([str(i - ord('a')), str(char_set[i])])
        return ''.join(res)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = defaultdict(list)
        for s in strs:
            hashed = self.get_hash(s)
            hmap[hashed].append(s)
        return hmap.values()




        