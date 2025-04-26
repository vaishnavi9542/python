def count_inversions(nums):
    def merge_sort_and_count(nums, start, end):
        if start >= end:
            return 0

        mid = (start + end) // 2
        count = merge_sort_and_count(nums, start, mid) + merge_sort_and_count(nums, mid + 1, end)
        j = mid + 1

        for i in range(start, mid + 1):
            while j <= end and nums[i] > nums[j]:
                j += 1
                count += (j - (mid + 1))

        temp = []
        left = start
        right = mid + 1
        while left <= mid and right <= end:
            if nums[left] <= nums[right]:
                temp.append(nums[left])
                left += 1
            else:
                temp.append(nums[right])
                right += 1

        temp.extend(nums[left:mid + 1])
        temp.extend(nums[right:end + 1])
        nums[start:end + 1] = temp
        return count
    return merge_sort_and_count(nums,0,len(nums)-1)
nums=list(map(int,input().split()))
print(count_inversions(nums))
    
