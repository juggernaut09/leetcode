class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness = sorted(happiness, reverse = True)
        ans, count, i = 0, 0, 0
        
        while k > 0:
            sub = (happiness[i] - count) if (happiness[i] - count) > 0 else 0
            ans += sub
            i += 1
            count += 1
            k -= 1
        return ans 