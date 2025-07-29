class Solution:
    def mySqrt(self, x: int) -> int:
        ''' res=int(sqrt(x))
        return res'''
        if x==0:
            return 0
        f,l=1,x
        while f<=l:
            mid=f+(l-f)//2
            if mid == x//mid:
                return mid
            elif mid >x//mid:
                l=mid-1
            else: 
                f=mid+1
        return l
        
        
