def twoSum(nums,target):
        n=len(nums)
        for i in range(n-1):
            for j in range(i+1,n):
                if nums[i]+nums[j]==target:
                    return [i,j]
        return[]  
nums=list(map(int,input().split()))
target=int(input())
print(twoSum(nums,target)
