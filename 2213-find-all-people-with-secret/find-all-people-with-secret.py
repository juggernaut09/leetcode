class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        secret = set([0, firstPerson])
        time_map = {}

        # create Adjacency List
        for src, dst, t in meetings:
            if t not in time_map:
                time_map[t] = defaultdict(list)
            time_map[t][src].append(dst)
            time_map[t][dst].append(src)
        
        def dfs(src, adj):
            if src in visit:
                return
            visit.add(src)
            secret.add(src)
            for nei in adj[src]:
                dfs(nei, adj)

        # Travsers trough Adjacency List
        for t in sorted(time_map.keys()):
            visit = set()
            for src in time_map[t]:
                if src in secret:
                    dfs(src, time_map[t])

        return list(secret)