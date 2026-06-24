class Solution:
    MOD = 10**9 + 7

    def multiply(self, A, B):
        n = len(A)
        C = [[0] * n for _ in range(n)]

        for i in range(n):
            for k in range(n):
                if A[i][k] == 0:
                    continue

                a = A[i][k]

                for j in range(n):
                    if B[k][j]:
                        C[i][j] = (C[i][j] + a * B[k][j]) % self.MOD

        return C

    def power(self, base, exp):
        n = len(base)

        res = [[0] * n for _ in range(n)]
        for i in range(n):
            res[i][i] = 1

        while exp:
            if exp & 1:
                res = self.multiply(res, base)

            base = self.multiply(base, base)
            exp >>= 1

        return res

    def apply(self, M, vec):
        n = len(M)
        res = [0] * n

        for i in range(n):
            cur = 0
            row = M[i]

            for j in range(n):
                if row[j]:
                    cur = (cur + row[j] * vec[j]) % self.MOD

            res[i] = cur

        return res

    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        m = r - l + 1
        S = 2 * m

        T = [[0] * S for _ in range(S)]

        # U_new[v] = sum(D[u]) for u < v
        for v in range(m):
            for u in range(v):
                T[v][m + u] = 1

        # D_new[v] = sum(U[u]) for u > v
        for v in range(m):
            for u in range(v + 1, m):
                T[m + v][u] = 1

        # State for length = 2
        state = [0] * S

        for v in range(m):
            state[v] = v              # U[v]
            state[m + v] = m - 1 - v # D[v]

        P = self.power(T, n - 2)
        final_state = self.apply(P, state)

        return sum(final_state) % self.MOD
