class Solution:
    def pivotInteger(self, n: int) -> int:
        nums = [i for i in range(1, n+1)]

        for i in range(len(nums)):
            if sum(nums[:i+1]) == sum(nums[i:]):
                return nums[i]
        return -1