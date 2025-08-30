class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=''.join(e.lower() for e in s if e.isalnum())
        return s==s[::-1]
        
