class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sort_scores = sorted(score, reverse = True)
        hmap = {}
        for i, s in enumerate(sort_scores):
            if i == 0:
                hmap[s] = "Gold Medal"
            elif i == 1:
                hmap[s] = "Silver Medal"
            elif i == 2:
                hmap[s] = "Bronze Medal"
            else:
                hmap[s] = i + 1
        # print(hmap)

        answer = []
        for i in score:
            answer.append(str(hmap[i]))
        return answer
