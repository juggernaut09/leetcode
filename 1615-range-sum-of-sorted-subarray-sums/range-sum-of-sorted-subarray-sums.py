class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        res = []
        for i in range(len(nums)):
            j = i
            curr_sum = 0
            while j < len(nums):
                curr_sum += nums[j]
                res.append(curr_sum)
                j += 1

        res.sort()
        mod = 10**9 + 7
        return sum(res[left - 1 : right]) % mod