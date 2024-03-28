class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        hmap = {}
        left, right, longest_sub, n = 0, 0, 0, len(nums)

        while right < n:
            hmap[nums[right]] = hmap.get(nums[right], 0) + 1
            while hmap[nums[right]] > k:
                hmap[nums[left]] = hmap.get(nums[left], 0) - 1
                left += 1
            longest_sub = max(longest_sub, (right - left + 1))
            right += 1
        return longest_sub