class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        res_str = []
        word = ""
        for c in s:
            if c == " ":
                if len(word):
                    res_str.append(word)
                    word = ""
                continue
            word += c
        if len(word):
            res_str.append(word)
        return len(res_str[-1])

