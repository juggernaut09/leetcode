class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a, b = 0, int(c ** 0.5)
        while a <=b :
            curr_sum = a**2 + b**2
            if curr_sum == c:
                return True
            elif curr_sum < c:
                a += 1
            else:
                b -= 1
        return False
        