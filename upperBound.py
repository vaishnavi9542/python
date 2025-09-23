class Solution:
    def upperBound(self, arr, target):
        ans=len(arr)
        low=0
        high=len(arr)-1
        while(low<=high):
            mid=(low+high)//2
            if (arr[mid]>target):
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans
        
        
