class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counter = collections.Counter(arr)
        counter = dict(sorted(counter.items(), key = lambda item: item[1]))
        for key, value in counter.items():
            if k > value:
                k = k - value
                counter[key] = 0
            else:
                counter[key] = counter[key] - k
                k = 0
                break
        cnt = 0
        for key, value in counter.items():
            if value > 0:
                cnt += 1
        return cnt 




