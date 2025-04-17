def chocolate(N,jars):
  A=0
  for chocolate in jars:
    A+=(chocolate+2)//3
  return A

N=int(input())
jars=list(map(int,input()))
print(chocolate(N,jars))
