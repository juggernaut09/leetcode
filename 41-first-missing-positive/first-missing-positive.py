class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if 1 not in nums:
            return 1
        else:
            for i in range(len(nums)):
                if nums[i] <= 0 or nums[i] > len(nums):
                    nums[i] = 1

            for i in range(len(nums)):
                num = abs(nums[i])
                idx = num -1
                if nums[idx] < 0:
                    continue
                else:
                    nums[idx] = (-1 * nums[idx])

            for idx in range(len(nums)):
                if nums[idx] > 0:
                    return idx + 1
            
            return len(nums) + 1