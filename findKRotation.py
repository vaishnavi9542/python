class Solution:
    def findKRotation(self, nums):
        low=0
        high=len(nums)-1
        ans=float("inf")
        index=0
        while(low<=high):
            mid=(low+high)//2
            if (nums[low]<=nums[mid]):  #left half sorted
                if (nums[low]<ans) :
                    ans=nums[low]
                    index=low
                low=mid+1
            elif (nums[mid]<=nums[high]): #right half sorted
                if (nums[mid]<ans):
                    ans=nums[mid]
                    index=mid
                high=mid-1
        return index  
        
