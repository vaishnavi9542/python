class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        count={}
        for char in s:
            if char not in count:
                count[char]=1
            count[char]+=1
        values=list(count.values())
        return all(v==values[0] for v in values)

        
