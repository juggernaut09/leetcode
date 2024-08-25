class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        from collections import Counter
        counter = Counter(nums)
        return len(counter) != len(nums) 