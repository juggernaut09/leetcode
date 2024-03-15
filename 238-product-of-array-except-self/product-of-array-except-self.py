class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        #Calculate Prefix
        prefix_arr = [0] * len(nums)
        prefix_arr[0] = 1
        for i in range(1, len(nums)):
            prefix_arr[i] = nums[i-1] * prefix_arr[i-1]

        #calculate postfix
        postfix = 1
        answer = [0]*len(nums)
        for i in reversed(range(len(nums))):
            answer[i] = prefix_arr[i] * postfix
            postfix = postfix * nums[i]

        return answer
        

        

