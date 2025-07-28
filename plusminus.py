def plusMinus(arr):
    pos=0
    neg=0
    zero=0
    for i in arr:
        if i>0:
            pos+=1
        elif i<0:
            neg+=1
        else:
            zero+=1
    total=len(arr)
    print(pos/total)
    print(neg/total)
    print(zero/total)
arr=list(map(int,input().split()))
plusMinus(arr)
