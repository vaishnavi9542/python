def sum_of_prime(str):
    sum=0
    prime_list=('2','3','5','7')
    for char in str:
        if char in prime_list:
            sum+=int(char)
    return sum
str=input()
print(sum_of_prime(str))
            
