class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.prefix = self.nums
        for k in range(1, len(self.prefix)):
            self.prefix[k] += self.prefix[k - 1]

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right] - 0 if left == 0 else self.prefix[right] - self.prefix[left - 1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)