class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        count1=count2=0
        val1=val2=None
        for num in nums:
            if num==val1:
                count1+=1
            elif num==val2:
                count2+=1
            elif count1==0:
                val1=num
                count1=1
            elif count2==0:
                val2=num
                count2=1
            else:
                count1-=1
                count2-=1
        arr=[]
        n=len(nums)
        if nums.count(val1)>n//3:
            arr.append(val1)
        if nums.count(val2)>n//3:
            arr.append(val2)
        return arr
        
        
