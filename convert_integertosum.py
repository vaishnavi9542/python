class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        def hasZero(x: int) -> bool:
            return '0' in str(x)

        a = 1
        while a < n:   
            b = n - a
            if not hasZero(a) and not hasZero(b):
                return [a, b]
            a += 1
        return []

        
