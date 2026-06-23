s=input()
vowel=set("aeiouAEIOU")
words=s.split()
best=""
for word in words:
    if len(word)%2==0 and word[0] in vowel:
        if len(word)>len(best):
            best=word
print(best if best else "00")
        
