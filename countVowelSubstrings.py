class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        vowels=set('aeiou')
        n=len(word)
        count=0
        if n<5:
            return 0
        for i in range(n):
            if word[i] in vowels:
                uniq=set()
                for j in range(i,n):
                    if word[j] in vowels:
                        uniq.add(word[j])
                        if len(uniq)==5:
                            count+=1
                    else:
                        break
        return count
                
            





        
