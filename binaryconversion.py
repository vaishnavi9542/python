class Solution:
    def baseNeg2(self, n: int) -> str:
        res=[]
        if n==0:
            return "0"
        while(n!=0):
            rem=n% -2
            n//= -2
            if(rem<0):
                rem+=2
                n+=1
            res.append(str(rem))
        res="".join(res)
        return res[::-1]
        
