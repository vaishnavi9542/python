class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        # ans=float('-inf')
        for letter in letters:
            if letter>target:
                return letter
        return letters[0]
        
