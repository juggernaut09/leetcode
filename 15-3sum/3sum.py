class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []

        for i, num in enumerate(nums):
            if i > 0 and num == nums[i - 1]:
                continue
            left, right = i + 1, len(nums) - 1

            while left < right:
                _sum = nums[i] + nums[left] + nums[right]

                if left > i +1 and nums[left] == nums[left - 1]:
                    left += 1
                    continue

                if right < len(nums) - 1 and nums[right] == nums[right + 1]:
                    right -= 1
                    continue

                if not _sum:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                elif _sum > 0:
                    right -= 1
                else:
                    left += 1

        return res

