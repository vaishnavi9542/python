class Solution:
    def reverse(self, x: int) -> int:
        sign=-1 if x<0 else 1
        s=int(str(abs(x))[::-1])*sign
        if s < -2**31 or s > 2**31 - 1:
            return 0
        return s
        
