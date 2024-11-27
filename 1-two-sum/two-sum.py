class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hmap = {}
        # for i in range(len(nums)):
        #     required = target - nums[i]
        #     if required in hmap:
        #         return [hmap[required], i]
        #     else:
        #         hmap[nums[i]] = i

        # return []
        nums = [(val, idx) for idx, val in enumerate(nums)]
        nums.sort()
        
        left, right = 0, len(nums) - 1

        while left < right:
            _sum = nums[left][0] + nums[right][0]
            if  _sum == target:
                return [nums[left][1], nums[right][1]]
            elif _sum > target:
                right -= 1
            else:
                left += 1

        return [] 


        return []
