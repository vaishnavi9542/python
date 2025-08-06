class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        vowels=set('aeiou')
        n=len(s)
        beautiful=0
        for i in range(n):
            v_count=0
            c_count=0
            for j in range(i,n):
                if s[j] in vowels:
                    v_count+=1
                else:
                    c_count+=1
                if v_count==c_count and (v_count*c_count)%k==0 :
                    beautiful+=1
        return beautiful
            

        
