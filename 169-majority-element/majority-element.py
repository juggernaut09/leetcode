class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hmap = {}
        for i in nums:
            if str(i) in hmap.keys():
                hmap[str(i)] += 1
            else:
                hmap[str(i)] = 1
            if hmap[str(i)] > len(nums)/2:
                    return i
        return -1