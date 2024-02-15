class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        # Bruteforce Backward Iteration
        nums.sort()
        _sum = sum(nums)
        for i in range(len(nums) - 1, 1, -1):
            _sum -= nums[i]
            if _sum > nums[i]:
                return _sum + nums[i]
        return -1