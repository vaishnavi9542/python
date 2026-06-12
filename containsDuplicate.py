class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums)!=len(set(nums))
        # res=[]
        # for i in nums:
        #     if i in res:
        #         return True
        #     else:
        #         res.append(i)
        # return False
        
