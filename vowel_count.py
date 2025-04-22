def vowel_count(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = {}

    for letter in s:
        if letter in vowels:
            if letter in count:
                count[letter] += 1
            else:
                count[letter] = 1

    max_vowels = 0
    result_vowel = ''
    for i in count:
        if count[i] > max_vowels:
            max_vowels = count[i]
            result_vowel = i

    return result_vowel

s = input()
print(vowel_count(s))
