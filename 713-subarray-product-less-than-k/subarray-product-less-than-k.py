class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0

        left, right, product, count = 0, 0, 1, 0

        while right < len(nums):
            product = product * nums[right]
            while product >= k:
                product = product // nums[left]
                left += 1
            count = count + (right - left + 1)
            right += 1
        return count