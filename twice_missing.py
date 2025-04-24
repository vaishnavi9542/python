def twice_missing(nums):
    n = len(nums)
    count = {}
    duplicate = -1
    missing = -1

   
    for num in nums:
        count[num] = count.get(num, 0) + 1

   
    for i in range(1, n + 1):
        if i in count:
            if count[i] > 1:
                duplicate = i
        else:
            missing = i

    return [duplicate, missing]
nums = list(map(int, input().split()))
print(twice_missing(nums))
