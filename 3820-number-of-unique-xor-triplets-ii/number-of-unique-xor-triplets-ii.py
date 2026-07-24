class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        vals = list(set(nums))
        MAX = 2048

        # all XORs obtainable from two values (repetition allowed)
        two = [False] * MAX
        for a in vals:
            for b in vals:
                two[a ^ b] = True

        # extend with a third value
        ans = [False] * MAX
        for x in range(MAX):
            if two[x]:
                for c in vals:
                    ans[x ^ c] = True

        return sum(ans)