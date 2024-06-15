class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        import heapq
        projects = sorted(zip(capital, profits), key = lambda x : x[0])

        heap = []  
        i = 0

        for _ in range(k):
            while i < len(projects) and projects[i][0] <= w:
                heapq.heappush(heap, -projects[i][1])
                i += 1
            if heap:
                w -= heapq.heappop(heap)
            else:
                break

        return w


        