class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False

        bracketMap = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        } 
        stack = []
        for bracket in s:
            if bracket in bracketMap:
                if stack and bracketMap[bracket] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(bracket)

        return len(stack) == 0