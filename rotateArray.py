class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n=len(nums)
        k=k%n
        nums[:]=nums[-k:]+nums[:-k]
        '''def rev(left,right):
            while left<right:
                nums[left],nums[right]=nums[right],nums[left]
                left+=1
                right-=1
        rev(0,n-1)
        rev(0,k-1)
        rev(k,n-1)'''


        """
        Do not return anything, modify nums in-place instead.
        """
        
