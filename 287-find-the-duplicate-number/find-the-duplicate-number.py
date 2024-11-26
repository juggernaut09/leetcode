class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = nums[0], nums[0]


        # Detecting cycle
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast: # Cycle detected
                break

        # Reset the slow to get the duplicate number
        slow = nums[0]

        while slow != fast: # slow and fast matches at the duplicate number
            slow = nums[slow]
            fast = nums[fast]

        return slow