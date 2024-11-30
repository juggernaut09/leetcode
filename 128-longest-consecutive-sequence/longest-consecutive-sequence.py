class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not len(nums):
            return 0
            
        hashSet = set(nums)
        max_len = 0

        for num in nums:
            # start of the sequence
            if num - 1 not in hashSet:
                longest_streak = 1
                while num + longest_streak in hashSet:
                    longest_streak += 1

                max_len = max(max_len, longest_streak)

        return max_len