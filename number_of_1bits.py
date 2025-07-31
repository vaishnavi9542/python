class Solution:
    def hammingWeight(self, n: int) -> int:
        count=0
        '''if (n&(1<<i))!=0:
            count+=1
        return count'''
        '''while(n):
            n=n&(n-1)
            count+=1
        return count'''
        count=0
        n=bin(n)[2:]
        for i in n:
            if i=='1':
                count+=1
        return count

        
