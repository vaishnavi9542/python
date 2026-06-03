from typing import List

class FenwickMax:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def update(self, idx, val):
        idx += 1
        while idx <= self.n:
            self.bit[idx] = max(self.bit[idx], val)
            idx += idx & -idx

    def query(self, idx):
        res = 0
        idx += 1
        while idx > 0:
            res = max(res, self.bit[idx])
            idx -= idx & -idx
        return res


class FenwickSum:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def add(self, idx, val):
        idx += 1
        while idx <= self.n:
            self.bit[idx] += val
            idx += idx & -idx

    def query(self, idx):
        s = 0
        idx += 1
        while idx > 0:
            s += self.bit[idx]
            idx -= idx & -idx
        return s

    def kth(self, k):
        idx = 0
        bitmask = 1 << (self.n.bit_length() - 1)

        while bitmask:
            nxt = idx + bitmask
            if nxt <= self.n and self.bit[nxt] < k:
                k -= self.bit[nxt]
                idx = nxt
            bitmask >>= 1

        return idx


class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        mx = max(q[1] for q in queries) + 1

        obstacles = {0, mx}
        for q in queries:
            if q[0] == 1:
                obstacles.add(q[1])

        pos = sorted(obstacles)

        left = [-1] * (mx + 1)
        right = [-1] * (mx + 1)

        for i in range(len(pos)):
            if i:
                left[pos[i]] = pos[i - 1]
            if i + 1 < len(pos):
                right[pos[i]] = pos[i + 1]

        bit_gap = FenwickMax(mx + 1)
        bit_cnt = FenwickSum(mx + 1)

        for p in pos:
            bit_cnt.add(p, 1)

        for i in range(1, len(pos)):
            bit_gap.update(pos[i], pos[i] - pos[i - 1])

        ans = []

        for q in reversed(queries):
            if q[0] == 1:
                x = q[1]

                l = left[x]
                r = right[x]

                bit_gap.update(r, r - l)

                right[l] = r
                left[r] = l

                bit_cnt.add(x, -1)

            else:
                x, sz = q[1], q[2]

                cnt = bit_cnt.query(x)
                pred = bit_cnt.kth(cnt) if cnt else 0

                best = max(bit_gap.query(x), x - pred)
                ans.append(best >= sz)

        return ans[::-1]
