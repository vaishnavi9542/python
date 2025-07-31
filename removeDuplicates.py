class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        i=0
        for j in range(i+1,len(nums)):
            if nums[j]!=nums[i]:
                i+=1
                nums[i]=nums[j]
        return i+1
        '''if not nums:
            return 0
        k=1
        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]:
                nums[k]=nums[i]
                k+=1
        return k'''
    ''' uniq=sorted(list(set(nums)))
        for i in range(len(uniq)):
            nums[i]=uniq[i]
        return len(uniq)'''
        
    
