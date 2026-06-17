class Solution:
    def processStr(self, s: str, k: int) -> str:
        lengths = []
        size = 0

        # Build only lengths
        for ch in s:
            if ch.islower():
                size += 1

            elif ch == "*":
                if size > 0:
                    size -= 1

            elif ch == "#":
                size *= 2

            elif ch == "%":
                pass

            lengths.append(size)

        if k >= size:
            return "."

        # Work backwards
        for i in range(len(s) - 1, -1, -1):
            ch = s[i]
            curr = lengths[i]
            prev = lengths[i - 1] if i > 0 else 0

            if ch.islower():
                if k == curr - 1:
                    return ch

            elif ch == "*":
                if k >= prev:
                    k = prev

            elif ch == "#":
                half = curr // 2
                if k >= half:
                    k -= half

            elif ch == "%":
                if curr > 0:
                    k = curr - 1 - k

        return "."
