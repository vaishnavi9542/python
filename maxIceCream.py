class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        count=0
        ans=0
        costs=sorted(costs)
        for i in costs:
            count+=i
            if count<=coins:
                ans+=1
        return ans




        
