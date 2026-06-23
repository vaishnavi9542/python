s="ABCabc"
def good_segments(s):
    if not s:
        return 0
    count=0
    currlen=1
    for i in range(1,len(s)):
        if s[i].isupper()==s[i-1].isupper():
            currlen+=1
        else:
            if currlen>1:
                count+=1
            currlen=1
    if currlen>1:
        count+=1
    return count
print(good_segments(s))
