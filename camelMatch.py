class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        def matches(query,pattern):
            i,j=0,0
            while i<len(query):
                if j<len(pattern) and query[i]==pattern[j]:
                    i+=1
                    j+=1
                elif query[i].islower():
                    i+=1
                else:
                    return False
            return j==len(pattern)
        return [matches(query,pattern) for query in queries]
                
