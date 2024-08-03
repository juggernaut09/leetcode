class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        def check_validity(nu: List[int]) -> bool:
            for i in range(0, len(nu) - 1):
                if nu[i] >= nu[i + 1]:
                    return False
            return True
        
        if check_validity(nums):
            return True
        
        flag = False
        for i in range(len(nums)):
            if check_validity(nums[:i] + nums[i+1:]):
                flag = True
        return flag
            

        # remove_operation = False
        
        # i = len(nums) - 1
        # while(i > 0):
        #     if nums[i] <= nums[i - 1]:
        #         if not remove_operation:
        #             nums.remove(nums[i - 1])
        #             remove_operation = True
        #             continue   
        #         else:
        #             return False
        #     i -= 1
        # return True

