class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        hmap = {}

        for num in nums1:
            hmap[num] = hmap.get(num, 0) + 1

        for num in nums2:
            if num in hmap.keys():
                return num
        return -1