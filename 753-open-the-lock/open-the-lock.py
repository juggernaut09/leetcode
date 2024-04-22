class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def children(lock):
            res = []
            for i in range(4):
                digit = str((int(lock[i]) + 1) % 10)
                res.append(lock[:i] + digit + lock[i + 1 :])
                digit = str((int(lock[i]) - 1 + 10) % 10)
                res.append(lock[:i] + digit + lock[i + 1 :])
            return res

        if "0000" in deadends:
            return -1
        visited = set(deadends)
        queue = [["0000", 0]] # [state, turns]
        while queue:
            curr, turns = queue.pop(0)
            if curr == target:
                return turns
            for child in children(curr):
                if not child in visited:
                    visited.add(child)
                    queue.append([child, turns + 1])

        return - 1

