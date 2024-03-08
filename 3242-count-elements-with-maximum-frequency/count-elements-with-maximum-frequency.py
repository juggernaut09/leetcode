class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        hmap = {}
        for num in nums:
            hmap[num] = hmap.get(num, 0) + 1
        
        max = 0
        res = 0
        for key, value in hmap.items():
            if value > max:
                max = value
                res = value
            elif value == max:
                res += value

        return res
        