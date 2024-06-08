class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        hmap = {0 : -1}
        cum_sum = 0
        for i, num in enumerate(nums):
            cum_sum += num
            if k != 0:
                cum_sum %= k
            if cum_sum in hmap:
                if i - hmap[cum_sum] > 1:
                    return True
            else:
                hmap[cum_sum] = i
        return False