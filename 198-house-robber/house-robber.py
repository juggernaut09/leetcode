class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])

        prev1 = 0
        prev2 = 0

        for num in nums:
            current = max(prev1, num + prev2)
            prev2 = prev1
            prev1 = current

        return prev1