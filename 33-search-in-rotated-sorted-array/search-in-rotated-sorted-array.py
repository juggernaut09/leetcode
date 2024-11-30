class Solution:
    def search(self, nums: List[int], target: int) -> int:
        hmap = {num : i for i, num in enumerate(nums)}

        return hmap[target] if target in hmap else -1