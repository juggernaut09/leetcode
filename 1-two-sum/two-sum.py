class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}

        for i in range(len(nums)):
            required = target - nums[i]
            if required in hmap:
                return [hmap[required], i]
            else:
                hmap[nums[i]] = i

        return []
        
