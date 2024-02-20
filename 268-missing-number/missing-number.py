class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        req = [i for i in range(n+1)]
        for i in range(len(req)):
            if i < len(nums):
                if req[i] != nums[i]:
                    return req[i]
            else:
                return req[i]