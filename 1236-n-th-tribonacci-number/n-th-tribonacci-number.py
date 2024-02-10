class Solution:
    def tribonacci(self, n: int) -> int:
        return self.tribonacci_memo(n, [-1] * (n+1))

    def tribonacci_memo(self, i: int, memo: list[int]) -> int:
        if i == 0: return 0
        if i == 1 or i == 2: return 1
        if memo[i] < 0:
            memo[i] = self.tribonacci_memo(i-1, memo) + self.tribonacci_memo(i-2, memo) + self.tribonacci_memo(i-3, memo)
        return memo[i]
