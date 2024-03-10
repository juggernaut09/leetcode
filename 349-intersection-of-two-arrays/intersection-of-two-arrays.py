class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        st1 = set(nums1)
        res = set()

        for num in nums2:
            if num in st1:
                res.add(num)
        return list(res)

        