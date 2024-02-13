class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        X = 0
        for operation in operations:
            if operation[0] == '-' or operation[-1] == '-':
                X = X - 1
            elif operation[0] == '+' or operation[-1] == '+':
                X = X + 1
        return X