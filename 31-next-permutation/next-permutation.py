class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # find pivot
        n = len(nums)
        i = n - 2

        while i >=0 and nums[i] >= nums[i + 1]:
            i -= 1
        
        # find suffix
        if i >= 0:
            j = n - 1

            while j >= 0 and nums[j] <= nums[i]:
                j -= 1

            # swap nums[i] and nums[j]
            nums[i], nums[j] = nums[j], nums[i]

        # reverse the string from after i
        nums[i + 1:] = reversed(nums[i + 1 :])

        return nums
        