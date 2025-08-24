class Solution:
    def countAsterisks(self, s: str) -> int:
        count=0
        flag=0
        for i in s:
            if i=='|':
                flag=not flag
            elif not flag and i=='*': 
                count+=1
        return count

        
