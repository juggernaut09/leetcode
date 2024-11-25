class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        prefix_sum = 0
        mp = {
            0:1
        }

        for num in nums:
            prefix_sum += num

            if prefix_sum - k in mp:
                res += mp[prefix_sum - k]

            
            mp[prefix_sum] = mp.get(prefix_sum, 0) + 1
        return res