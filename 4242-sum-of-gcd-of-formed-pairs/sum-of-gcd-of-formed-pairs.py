class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        mx=0
        prefixGcd=[]
        for i in nums:
            mx=max(mx,i)
            prefixGcd.append(gcd(i,mx))
        prefixGcd.sort()
        ans=0
        l,r=0,len(prefixGcd)-1
        while l<r:
            ans+=gcd(prefixGcd[l],prefixGcd[r])
            l+=1
            r-=1
        return ans
        
        