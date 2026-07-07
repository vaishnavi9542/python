class Solution:
    def sumAndMultiply(self, n: int) -> int:
        res=""
        for i in str(n):
            if i!='0':
                res+=i
        if not res:
            return 0
        ans=0
        for i in res:
            ans+=int(i)
        return int(res)*ans
        # res=''.join(ch for ch in str(n)if ch!='0')
        # if not res:
        #     return 0
        # return int(res)*sum(int(ch)for ch in res)
            
        