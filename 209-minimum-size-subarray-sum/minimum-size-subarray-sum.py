class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        min_length = float("inf")

        left = 0
        curr_sum = 0

        for right in range(len(nums)):
            curr_sum += nums[right]


            while left <= right and curr_sum >= target:
                min_length = min(min_length, right - left + 1)
                curr_sum -= nums[left]
                left += 1

        return 0 if min_length == float("inf") else min_length

        
