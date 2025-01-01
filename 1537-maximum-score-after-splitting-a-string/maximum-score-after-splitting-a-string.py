class Solution:
    def maxScore(self, s: str) -> int:

        num_of_zeros = 0 # 
        num_of_ones = s.count('1')
        res = 0


        # loop untill the last but one element
        for i in range(len(s) - 1): 
            if s[i] == '0':
                # checking the char if it is a zero i.e 
                # adding 1 to num_of_zeros i.e to the left portion
                num_of_zeros += 1
            else:
                # if the char is 1, then the count of num_of_ones is deceremented by 1
                # i.e reducing the right portion. 
                num_of_ones -= 1
            
            # calculate the sum of num_of_zeros in te left portion with the num_of_ones 
            # in  the right portion
            res = max(res, num_of_zeros + num_of_ones)

        return res