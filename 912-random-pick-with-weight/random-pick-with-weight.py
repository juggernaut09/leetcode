class Solution:
    import random

    def __init__(self, w: List[int]):
        self.prefix_sum = []
        prefix = 0
        for weight in w:
            prefix += weight
            self.prefix_sum.append(prefix)

    def pickIndex(self) -> int:
        target = random.randint(1, self.prefix_sum[-1])

        left = 0
        right = len(self.prefix_sum) - 1

        while left < right:
            mid = (left + right) // 2

            if self.prefix_sum[mid] < target:                 
                left = mid + 1
            else:
                right = mid

        return left

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()