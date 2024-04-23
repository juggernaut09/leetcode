class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # create adj list
        adj = defaultdict(list)
        for src, dest in edges:
            adj[src].append(dest)
            adj[dest].append(src)
        
        if not len(adj) and n == 1:
            return [0]

        # count edges, leaves
        edge_count = {}
        leaves = deque()
        for node, neighbors in adj.items():
            edge_count[node] = len(neighbors)
            if edge_count[node] == 1:
                leaves.append(node)

        # Remove leaf nodes.

        while leaves:
            if n <= 2:
                return list(leaves)
            
            for i in range(len(leaves)):
                node = leaves.popleft()
                n -= 1
                for nei in adj[node]:
                    edge_count[nei] -= 1
                    if edge_count[nei] == 1:
                        leaves.append(nei)


        