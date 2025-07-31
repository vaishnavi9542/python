class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        return nums[n // 2]
        """count=0
        val=0
        for num in nums :
            if count==0:
                val=num
            if num==val:
                count+=1
            else:
                count-=1
        return val"""
