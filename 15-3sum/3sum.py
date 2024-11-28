class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # using three pointers i, j, k

        nums.sort()
        res = []
        
        n = len(nums)
        if n < 3:
            return []

        for i in range(n):

            # remove duplicate
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j = i + 1
            k = n - 1

            while j < k:
                _sum = nums[i] + nums[j] + nums[k]
                if _sum == 0:
                    res.append([nums[i], nums[j], nums[k]])
                    # remove duplicates in right pointer
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1
                    # remove duplicates in left pointer
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    
                    k -= 1
                    j += 1
                elif _sum > 0:
                    k -= 1
                else:
                    j += 1

        return res