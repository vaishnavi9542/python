def intersection(nums1, nums2):
    common_elements = []
    for i in nums1:
        for j in nums2:
            if i == j:
                common_elements.append(i)
                break  # Avoid adding duplicates if j appears multiple times
    return common_elements

nums1 = list(map(int, input().split()))
nums2 = list(map(int, input().split()))
print(intersection(nums1, nums2))
