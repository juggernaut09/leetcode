class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        hmap = {}
        for num in nums:
            hmap[num] = hmap.get(num, 0) + 1
        return [key for key, value in hmap.items() if value > 1]