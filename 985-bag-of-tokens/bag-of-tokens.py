class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        if not len(tokens): return 0
        tokens.sort()
        i, j = 0, len(tokens) - 1
        score = 0
        maxScore = 0
        while max(tokens):
            if power >= tokens[i]:
                power -= tokens[i]
                tokens[i] = 0
                score += 1
                maxScore = max(maxScore, score)
                i += 1
            elif score >= 1:
                score -= 1
                power += tokens[j]
                tokens[j] = 0
                j -= 1
            else:
                break
        return maxScore



        