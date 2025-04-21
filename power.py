def myPow(x,n):
  if n == 0:
    return 1
  result=1
  if n < 0:
    x = 1 / x
    n = -n
    result = 1
  while n:
    if n % 2:
      result *= x
    x *= x
    n //= 2
    return result

x=int(input())
n=int(input())
print(myPow(x,n))
        
