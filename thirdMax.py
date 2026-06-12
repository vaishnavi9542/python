class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = sorted(set(nums))   # remove duplicates

        if len(nums) < 3:
            return nums[-1]

        return nums[-3]
