s=input()
arr=list(map(int,input().split()))
n=len(arr)
def solve(s,arr,n):
    digit_set=set(arr)
    count=0
    for ch in s:
        ascii_v=str(ord(ch))
        for i in ascii_v:
            if int(i) in digit_set:
                count+=1
                break
    return count
print(solve(s,arr,n))
