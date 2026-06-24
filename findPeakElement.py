class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # return nums.index(max(nums))
        # maxi=float('-inf')
        # ans=0
        # for i in range(len(nums)):
        #     if nums[i]>maxi:
        #         maxi=nums[i]
        #         ans=i
        # return ans
        left=0
        right=len(nums)-1
        while left<right:
            mid=(left+right)//2
            if nums[mid]<nums[mid+1]:
                left=mid+1
            else:
                right=mid
        return left
        
