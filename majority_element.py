def majority(nums):
    n = len(nums)
    k = n // 2  # Ensure integer division
    count = {}

    for i in nums:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1

    for j in count:
        if count[j] > k:
            return j

nums = list(map(int, input().strip().split()))
print(majority(nums))
