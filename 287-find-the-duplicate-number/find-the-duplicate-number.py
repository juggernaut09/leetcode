class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hset = set([])
        for num in nums:
            if num in hset:
                return num
            else:
                hset.add(num)
        return -1