def plusOne(digits):
    res=int(''.join(map(str,digits)))
    res=res+1
    res1=list(map(int,str(res)))
    return res1
digits=list(map(int,input().split()))
print(plusOne(digits))
