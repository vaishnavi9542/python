class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        ans=x^y
        cnt=0
        while (ans!=0):
            rem=ans%2
            if(rem==1):
                cnt+=1
            ans=ans//2
        return cnt
        
