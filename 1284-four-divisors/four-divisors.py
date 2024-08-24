class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        def get_divisors(num):
            from math import sqrt
            divisors = []
            for d in range(1, int(sqrt(num)) + 1):
                if num % d == 0:
                    divisors.append(d)
                    divisors.append(num // d)
            return list(set(divisors))

        res = 0
        for num in nums:
            divisors = get_divisors(num)
            res += sum(divisors) if len(divisors) == 4 else 0
            
        return res