class Solution:
    def checkDivisibility(self, n: int) -> bool:
        s = str(n)
        total = 0
        prod = 1

        for i in s:
            digit = int(i)
            total += digit
            prod *= digit

        return n % (total + prod) == 0