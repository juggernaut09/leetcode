class Solution:
    def minOperations(self, logs: list[str]) -> int:
        path_stack: list[str] = []
        for log in logs:
            if log == "../":
                if path_stack:
                    path_stack.pop()
            elif log != "./":
                path_stack.append(log)

        return len(path_stack)
