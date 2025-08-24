class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in (s+s)[1:-1]
        '''v=s+s
        v=v[1::]+v[::-1]
        if s in v:
            return True
        return False'''

        
