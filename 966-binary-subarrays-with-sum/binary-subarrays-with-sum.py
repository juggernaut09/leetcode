class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        hmap = {0:1}
        res, i, curr_sum = 0, 0, 0
        while i < len(nums):
            curr_sum += nums[i]
            if curr_sum - goal in hmap.keys():
                res += hmap[curr_sum - goal]
                # hmap[curr_sum - goal] = hmap.get(curr_sum - goal , 0) + 1
            hmap[curr_sum] = hmap.get(curr_sum, 0) + 1
            i+=1
        return res