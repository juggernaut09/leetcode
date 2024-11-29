class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # prefix_i - k = prefix_j
        # if prefix_j is in prefix_map
        #  count += prefix_map[prefix_j]


        prefix_sum = 0
        prefix_map = {
            0 : 1
        }
        count = 0

        for num in nums:
            prefix_sum += num
            
            if prefix_sum - k in prefix_map:
                count += prefix_map[prefix_sum - k]

            prefix_map[prefix_sum] = prefix_map.get(prefix_sum, 0) + 1

        return count