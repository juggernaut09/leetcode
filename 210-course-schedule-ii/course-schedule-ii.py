class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        from collections import deque, defaultdict

        # create graph and in-degree
        in_degree = [0] * numCourses
        graph = defaultdict(list)

        for course, prereq in prerequisites:
            graph[prereq].append(course) # prereq -> course # after this prereq go to course.
            in_degree[course] += 1 # No. of prereqs to be completed for this course

        # find all courses with no prereqs
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        order = []

        while queue:
            course = queue.popleft()
            order.append(course)
            for neighbor in graph[course]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)



        return order if len(order) == numCourses else []



