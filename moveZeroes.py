class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        idx=0
        for num in range(len(nums)):
            if nums[num]!=0:
                nums[idx]=nums[num]
                idx+=1
        for i in range(idx,len(nums)):
            nums[i]=0
    
        """
        Do not return anything, modify nums in-place instead.
        """
        
