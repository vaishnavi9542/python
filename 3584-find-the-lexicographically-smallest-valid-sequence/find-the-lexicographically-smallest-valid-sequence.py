class Solution:
    def validSequence(self, word1: str, word2: str):
        n = len(word1)
        m = len(word2)

        # suf[j] = position in word1 used to match word2[j]
        # when matching word2[j:] from the right.
        suf = [-1] * m

        i = n - 1
        j = m - 1

        while i >= 0 and j >= 0:
            if word1[i] == word2[j]:
                suf[j] = i
                j -= 1
            i -= 1

        ans = []
        j = 0
        changed = False

        for i in range(n):
            if j == m:
                break

            if word1[i] == word2[j]:
                # Exact match.
                ans.append(i)
                j += 1

            elif not changed:
                # We can change this character.
                #
                # The remaining word2[j+1:]
                # must be exactly matchable.
                if j == m - 1 or (
                    suf[j + 1] != -1 and suf[j + 1] > i
                ):
                    ans.append(i)
                    j += 1
                    changed = True

        if j == m:
            return ans

        return []