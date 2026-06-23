s=input()
if not s:
    print(0)
else:
    count=0
    for i in range(len(s)-1):
        if s[i].isupper()!=s[i+1].isupper():
            count+=1
    print(count)
        
