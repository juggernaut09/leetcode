class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        visited = set()

        # adjacency list
        neighbours = {}
        if n == 1 and not len(edges):
            return True
            
        for src, dest in edges:
            if not src in neighbours:
                neighbours[src] = []
            if not dest in neighbours:
                neighbours[dest] = []
            
            if not dest in neighbours[src]:
                neighbours[src].append(dest)
            
            if not src in neighbours[dest]:
                neighbours[dest].append(src)

        queue = [source]

        while len(queue):
            curr_vert = queue.pop(0)

            if curr_vert in visited:
                continue

            visited.add(curr_vert)

            if destination in neighbours[curr_vert]:
                return True

            for neighbour in neighbours[curr_vert]:
                queue.append(neighbour)

        return False