class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        res=[]
        for i in range(nums[0],nums[-1]):
            if i not in nums:
                res.append(i)
        return res
        