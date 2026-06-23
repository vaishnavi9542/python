def find_action(input1,input2):
    act=set(input1.split())
    sent=input2.split()
    n=len(sent)
    for i, w in enumerate(sent):
        if w in act:
            if i+1<n:
                next=sent[i+1]
                if next.lower()=="the":
                    if i+2<n:
                        return f"{w}{sent[i+2]}"
                else:
                    return f"{w}{next}"
    return None
input1 = "turn open close switch"
input2 = "please the fan off"
print( find_action(input1,input2))
