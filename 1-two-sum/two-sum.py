class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}
        '''
        x + y = target
        target - x = y

        '''
        for i, n in enumerate(nums):
            y = target - n
            if y in prevMap:
                return [i, prevMap[y]]
            prevMap[n] = i    
        return