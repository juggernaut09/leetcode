class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hmap = {0:1}
        curr_sum, i, res = 0, 0, 0
        while i < len(nums):
            curr_sum += nums[i]
            if curr_sum - k in hmap.keys():
                res += hmap[curr_sum - k]
            hmap[curr_sum] = hmap.get(curr_sum, 0) + 1
            i += 1
        return res