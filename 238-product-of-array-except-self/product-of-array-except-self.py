class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        res = [0] * len(nums)

        # calculate prefix
        prefix = 1
        for i in range(len(nums)):
            res [i] = prefix * nums[i]
            prefix *= nums[i]

        # calculate the postfix
        postfix = 1
        for i in range(len(res) - 1, -1, -1):
            if i == 0:
                res[i] = 1 * postfix
                break
            res[i] = res[i - 1] * postfix
            postfix *= nums[i]

        return res

