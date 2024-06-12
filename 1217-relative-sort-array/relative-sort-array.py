class Solution:
    def relativeSortArray(self, arr1, arr2):
        from collections import defaultdict

        counter = defaultdict(int)
        remaining = []
        res = []
        for num in arr2:
            counter[num] = 0

        for num in arr1:
            if num in counter.keys():
                counter[num] += 1
            else:
                remaining.append(num)

        for num in arr2:
            res.extend([num] * counter[num])
        
        remaining.sort()
        res.extend(remaining)
        return res
