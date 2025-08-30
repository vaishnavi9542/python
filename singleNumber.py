class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        '''dic={}
        for num in nums:
            if num not in dic:
                dic[num]=1
            else:
                dic[num]+=1
        for key in dic:
            if dic[key]==1:
                return key'''
        result=0
        for num in nums:
            result^=num
        return result
        
