from typing import List

class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        arr = sorted((nums[i], i) for i in range(n))

        pos = [0] * n
        values = [0] * n
        comp = [0] * n

        cid = 0
        for i, (v, idx) in enumerate(arr):
            values[i] = v
            pos[idx] = i
            if i and v - values[i - 1] > maxDiff:
                cid += 1
            comp[i] = cid

        # next reachable position
        nxt = [0] * n
        j = 0
        for i in range(n):
            while j + 1 < n and values[j + 1] - values[i] <= maxDiff:
                j += 1
            nxt[i] = j
            if j == i:
                j += 1

        LOG = n.bit_length()
        up = [nxt]

        for _ in range(1, LOG):
            prev = up[-1]
            cur = [0] * n
            for i in range(n):
                cur[i] = prev[prev[i]]
            up.append(cur)

        ans = []

        for u, v in queries:
            if u == v:
                ans.append(0)
                continue

            l = pos[u]
            r = pos[v]

            if l > r:
                l, r = r, l

            if comp[l] != comp[r]:
                ans.append(-1)
                continue

            cur = l
            dist = 0

            for k in range(LOG - 1, -1, -1):
                nx = up[k][cur]
                if nx < r:
                    cur = nx
                    dist += 1 << k

            ans.append(dist + 1)

        return ans