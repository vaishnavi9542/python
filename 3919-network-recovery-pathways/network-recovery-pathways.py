from typing import List
from collections import defaultdict, deque

class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        
        n = len(online)
        
        # build graph
        def build_graph(min_edge):
            g = defaultdict(list)
            indeg = [0] * n
            
            for u, v, w in edges:
                if w >= min_edge and online[u] and online[v]:
                    g[u].append((v, w))
                    indeg[v] += 1
            
            return g, indeg
        
        # check if valid path exists with min edge >= mid
        def can(mid):
            g, indeg = build_graph(mid)
            
            # topo sort
            dq = deque()
            for i in range(n):
                if indeg[i] == 0 and online[i]:
                    dq.append(i)
            
            topo = []
            
            while dq:
                u = dq.popleft()
                topo.append(u)
                for v, _ in g[u]:
                    indeg[v] -= 1
                    if indeg[v] == 0:
                        dq.append(v)
            
            # DP shortest path in DAG
            INF = float('inf')
            dist = [INF] * n
            dist[0] = 0
            
            for u in topo:
                if dist[u] == INF:
                    continue
                for v, w in g[u]:
                    dist[v] = min(dist[v], dist[u] + w)
            
            return dist[n - 1] <= k
        
        # binary search on answer
        lo, hi = 0, max((w for _, _, w in edges), default=0)
        ans = -1
        
        while lo <= hi:
            mid = (lo + hi) // 2
            
            if can(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1
        
        return ans