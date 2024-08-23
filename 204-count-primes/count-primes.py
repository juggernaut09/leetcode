class Solution:
    def countPrimes(self, n: int) -> int:
        if n == 0 or n == 1:
            return 0
            
        primes = [True] * n

        primes[0], primes[1] = False, False

        for i in range(2, n):
            if primes[i]:
                    for multiple in range(2 * i, n, i):
                        primes[multiple] = False

        return sum(primes)