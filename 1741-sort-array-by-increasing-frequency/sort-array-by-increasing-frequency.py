class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        d=Counter(nums)
        res=[]
        new_l=sorted(d.items(),key=lambda x:(x[1],-x[0]))
        for key,value in new_l:
            for _ in range(value):
                res.append(key)
        return res
        