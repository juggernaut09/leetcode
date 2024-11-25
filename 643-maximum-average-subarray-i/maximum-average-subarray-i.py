class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum =  sum(nums[:k])
        maxAvg = float(window_sum/k)

        for i in range(len(nums) - k):
            window_sum = window_sum - nums[i] + nums[i + k]
            window_avg = float(window_sum/k)
            maxAvg = max(window_avg, maxAvg)
            
        return maxAvg
                

        