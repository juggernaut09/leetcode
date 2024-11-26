class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mp = {}

        stack = []

        for num in nums2:
            while stack and num > stack[-1]:
                mp[stack.pop()] = num
            stack.append(num)

        
        while stack:
            mp[stack.pop()] = -1

        return [mp[num] for num in nums1]