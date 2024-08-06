class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        from collections import Counter

        counter = Counter(arr)
        
        for ele in arr:
            if counter[ele] == 1:
                k -= 1
            if k == 0:
                return ele
        return ''