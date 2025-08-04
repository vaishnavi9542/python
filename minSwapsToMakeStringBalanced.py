class Solution:
    def minSwaps(self, s: str) -> int:
        count=0
        for i in s:
            if i  is '[':
                count+=1
            else:
                if count>0:
                    count-=1
        return (count+1)//2
        
