class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        if n == 0:
            return [-1, -1]
        left, right = 0, n - 1
        while left < n and nums[left] != target:
            left += 1
        if left == n:
            return [-1, -1]
        while right >= 0 and nums[right] != target:
            right -= 1

        return [left, right]
