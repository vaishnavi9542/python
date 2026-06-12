from collections import defaultdict, deque
from typing import List

class Solution:
    def assignEdgeWeights(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        n = len(edges) + 1
        LOG = (n).bit_length()

        # Build graph
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # depth and parent
        depth = [0] * (n + 1)
        parent = [[0] * (n + 1) for _ in range(LOG)]

        # BFS from root = 1
        q = deque([1])
        visited = [False] * (n + 1)
        visited[1] = True

        while q:
            node = q.popleft()

            for nei in graph[node]:
                if not visited[nei]:
                    visited[nei] = True
                    depth[nei] = depth[node] + 1
                    parent[0][nei] = node
                    q.append(nei)

        # Binary lifting
        for j in range(1, LOG):
            for i in range(1, n + 1):
                parent[j][i] = parent[j - 1][parent[j - 1][i]]

        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u

            # Bring u to same level
            diff = depth[u] - depth[v]

            for j in range(LOG):
                if diff & (1 << j):
                    u = parent[j][u]

            if u == v:
                return u

            for j in range(LOG - 1, -1, -1):
                if parent[j][u] != parent[j][v]:
                    u = parent[j][u]
                    v = parent[j][v]

            return parent[0][u]

        # Precompute powers of 2
        pow2 = [1] * n
        for i in range(1, n):
            pow2[i] = (pow2[i - 1] * 2) % MOD

        ans = []

        for u, v in queries:
            ancestor = lca(u, v)

            edges_count = (
                depth[u]
                + depth[v]
                - 2 * depth[ancestor]
            )

            if edges_count == 0:
                ans.append(0)
            else:
                ans.append(pow2[edges_count - 1])

        return ans
