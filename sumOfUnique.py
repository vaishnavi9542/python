class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        total=0
        uniq=[]
        dup=[]
        for i in nums:
            if i not in uniq and i not in dup:
                uniq.append(i)
            elif i in uniq:
                uniq.remove(i)
                dup.append(i)
        total=sum(uniq)
        return total
        
