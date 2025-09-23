def nth_root(n,m):
    # for i in range(1,m+1):
    #     if(i**n==m):
    #         return i
    #     elif(i**n>m):
    #         break
    # return -1
    low=1
    high=m
    while low<=high:
        mid=(low+high)//2
        if mid**n<m:
            low=mid+1
        elif mid**n>m:
            high=mid-1
        else:
            return mid
    return -1
n=int(input())
m=int(input())
print(nth_root(n,m))
