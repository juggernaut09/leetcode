class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter
        if len(s1) > len(s2):
            return False

        countS1 = Counter(s1)
        windowCounter = Counter()

        for i in range(len(s2)):
            char = s2[i]

            windowCounter[char] = windowCounter.get(char, 0) + 1

            if i >= len(s1):
                left_char = s2[i - len(s1)]
                windowCounter[left_char] -= 1
                if windowCounter[left_char] == 0:
                    del windowCounter[left_char]

            if windowCounter == countS1:
                return True

        return False
                
