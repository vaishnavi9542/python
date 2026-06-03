from bisect import bisect_right
from typing import List

class Solution:
    def earliestFinishTime(
        self,
        landStartTime: List[int],
        landDuration: List[int],
        waterStartTime: List[int],
        waterDuration: List[int]
    ) -> int:

        def calc(firstS, firstD, secondS, secondD):
            rides = sorted(zip(secondS, secondD))
            starts = [s for s, d in rides]
            n = len(rides)

            # prefix minimum duration
            pref = [0] * n
            pref[0] = rides[0][1]

            for i in range(1, n):
                pref[i] = min(pref[i - 1], rides[i][1])

            # suffix minimum of (start + duration)
            suff = [0] * n
            suff[-1] = rides[-1][0] + rides[-1][1]

            for i in range(n - 2, -1, -1):
                suff[i] = min(
                    suff[i + 1],
                    rides[i][0] + rides[i][1]
                )

            ans = float("inf")

            for s, d in zip(firstS, firstD):
                finish = s + d

                idx = bisect_right(starts, finish)

                # already-open rides
                if idx > 0:
                    ans = min(ans, finish + pref[idx - 1])

                # rides opening later
                if idx < n:
                    ans = min(ans, suff[idx])

            return ans

        return min(
            calc(
                landStartTime,
                landDuration,
                waterStartTime,
                waterDuration
            ),
            calc(
                waterStartTime,
                waterDuration,
                landStartTime,
                landDuration
            )
        )
