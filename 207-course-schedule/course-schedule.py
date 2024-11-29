class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
            from collections import defaultdict
            graph = defaultdict(list)

            for course, prereq in prerequisites:
                graph[course].append(prereq)

            state = [0] * numCourses

            # states: 0 = Unvisited, 1 = visiting, 2 = visited

            def hasCycle(vertex):
                if state[vertex] == 1:
                    return True
                if state[vertex] == 2:
                    return False

                state[vertex] = 1
                for neigh in graph[vertex]:
                    if hasCycle(neigh):
                        return True

                state[vertex] = 2
                return False

            for v in range(numCourses):
                if state[v] == 0 and hasCycle(v):
                    return False

            return True

