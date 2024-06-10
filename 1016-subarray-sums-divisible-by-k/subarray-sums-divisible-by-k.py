class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        hashmap = {0: 1}
        cum_sum = 0
        res = 0
        for num in nums:
            cum_sum += num
            mod_sum = cum_sum % k
            if mod_sum in hashmap:
                res += hashmap[mod_sum]
            hashmap[mod_sum] = hashmap.get(mod_sum, 0) + 1
        return res