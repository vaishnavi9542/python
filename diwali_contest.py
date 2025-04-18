def party(N,P):
  leftover_time=240-P
  count=0
  time_left=0
  for i in range(1,N+1):
    time_left+=(5*i)
    if time_left<=leftover_time:
      count+=1
    else:
      break
  return count
N=int(input())
P=int(input())
print(party(N,P))
