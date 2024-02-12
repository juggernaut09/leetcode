class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hmap = {}
        for i in nums:
            hmap[str(i)] = hmap.get(str(i), 0) + 1
            if hmap[str(i)] > len(nums)/2:
                    return i
        return -1