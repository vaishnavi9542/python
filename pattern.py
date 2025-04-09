n=int(input())
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for k in range(1,i*2):
        print(chr(48+i),end="")
    print()
