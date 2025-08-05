class Solution:
    def countAndSay(self, n: int) -> str:
        if n==1:
            return '1'
        prev="1"
        for i in range(2,n+1):
            count=1
            res=""
            for j in range(1,len(prev)):
                if prev[j]==prev[j-1]:
                    count+=1
                else:
                    res+=str(count)+prev[j-1]
                    count=1
            res+=str(count)+prev[-1]
            prev=res
        return prev
        
