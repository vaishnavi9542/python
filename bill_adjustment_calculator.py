n=3
m=[10,20,30]
c=[2,3,5]
bill=300
import math
def calculate(n,m,c,bill):
    initial = sum(m1*c1 for m1,c1 in zip(m,c))
    if initial == bill:
        return -1
    sum_c = sum(c)
    diff = abs(bill-initial)
    steps = math.ceil(diff/sum_c)
    return steps
print(calculate(n,m,c,bill))
