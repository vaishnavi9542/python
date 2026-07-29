from collections import Counter
from math import comb

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        freq = Counter(s)

        half = [0] * 26
        mid = ""

        for ch, c in freq.items():
            half[ord(ch) - 97] = c // 2
            if c & 1:
                mid = ch

        LIMIT = k
        total = sum(half)

        # Returns min(number of distinct permutations, LIMIT + 1)
        def count(cnt):
            rem = sum(cnt)
            ans = 1
            for x in cnt:
                if x:
                    ans *= comb(rem, x)
                    if ans > LIMIT:
                        return LIMIT + 1
                    rem -= x
            return ans

        ways = count(half)
        if ways < k:
            return ""

        left = []

        for _ in range(total):
            for i in range(26):
                if half[i] == 0:
                    continue

                half[i] -= 1
                ways = count(half)

                if ways >= k:
                    left.append(chr(i + 97))
                    break
                else:
                    k -= ways
                    half[i] += 1

        left = "".join(left)
        return left + mid + left[::-1]