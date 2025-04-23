def majority(nums):
    n = len(nums)
    k = n // 3
    count = {}
    for i in nums:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    elements = []
    for j in count:
        if count[j] > k:
            elements.append(j)
    return elements
nums=list(map(imt,input().split()))
print(majority(nums))

