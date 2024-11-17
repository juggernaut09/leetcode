class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
    
        res = [0] * len(nums)

        # calculate prefix
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]


        # Calculate postfix
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] = res[i] * postfix
            postfix = postfix * nums[i]

        return res


