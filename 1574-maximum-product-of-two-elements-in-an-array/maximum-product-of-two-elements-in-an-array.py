class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        import heapq
        heap = []
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                product = (nums[i]-1)*(nums[j]-1)
                heapq.heappush(heap, -1 * product)

        return -1 * heapq.heappop(heap)

