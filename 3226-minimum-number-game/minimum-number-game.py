class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        import heapq
        heap, arr = [], []
        nums = sorted(nums, reverse = True)
        while len(nums):
            heapq.heappush(heap, -1 * nums.pop()) # Alice
            heapq.heappush(heap, -1 * nums.pop()) # Bob
            arr.append(-1 * heapq.heappop(heap))
            arr.append(-1 * heapq.heappop(heap))
        return arr
            

