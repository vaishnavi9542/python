class Solution:
    def stoneGameII(self, piles):
        n = len(piles)

        # suffix[i] = total stones from i to n-1
        suffix = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]

        memo = {}

        def dp(i, M):
            # All remaining piles can be taken
            if i >= n:
                return 0

            if (i, M) in memo:
                return memo[(i, M)]

            # Can take all remaining piles
            if i + 2 * M >= n:
                memo[(i, M)] = suffix[i]
                return suffix[i]

            best = 0

            # Try taking X piles
            for X in range(1, 2 * M + 1):
                # Stones taken by current player
                taken = suffix[i] - suffix[i + X]

                # Opponent's best result
                opponent = dp(i + X, max(M, X))

                # Current player's total
                current = taken + (
                    suffix[i + X] - opponent
                )

                best = max(best, current)

            memo[(i, M)] = best
            return best

        return dp(0, 1)