class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        first_upper = {}
        last_lower = {}
        
        for i, ch in enumerate(word):
            if ch.islower():
                last_lower[ch] = i
            else:
                ch_lower = ch.lower()
                if ch_lower not in first_upper:
                    first_upper[ch_lower] = i
        
        count = 0
        
        for ch in last_lower:
            if ch in first_upper and last_lower[ch] < first_upper[ch]:
                count += 1
        
        return count
