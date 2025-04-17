import math
import os
import random
import re
import sys



def loop(n):
    n = int(input().strip())
    for i in range(1,11):
        print( f"{n}", 'x', f"{i}" , '= ' f"{n*i}" )

n=int(input())
print(loop(n))
