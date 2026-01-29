class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=2:
            return n
        # return self.climbstairs(n-1)+self.climbStairs(n+2)
        first=1
        second=2
        for i in range(3,n+1):
            current=first+second
            first=second
            second=current
        return second
