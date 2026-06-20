class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:

        # Building 1 always has height 0
        restrictions.append([1, 0])

        # Add restriction for last building
        restrictions.append([n, n - 1])

        # Sort by building index
        restrictions.sort()

        m = len(restrictions)

        # Left → Right pass
        for i in range(1, m):
            prev_id, prev_h = restrictions[i - 1]
            curr_id, curr_h = restrictions[i]

            restrictions[i][1] = min(
                curr_h,
                prev_h + (curr_id - prev_id)
            )

        # Right → Left pass
        for i in range(m - 2, -1, -1):
            next_id, next_h = restrictions[i + 1]
            curr_id, curr_h = restrictions[i]

            restrictions[i][1] = min(
                curr_h,
                next_h + (next_id - curr_id)
            )

        # Find maximum possible peak
        ans = 0

        for i in range(1, m):
            id1, h1 = restrictions[i - 1]
            id2, h2 = restrictions[i]

            distance = id2 - id1

            # Maximum peak inside interval
            peak = (h1 + h2 + distance) // 2

            ans = max(ans, peak)

        return ans
