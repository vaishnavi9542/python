class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        val_dict={'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        res=['']
        if not digits or digits=='1':
            return []
        for i in digits:
            temp=[]
            for j in res:
                for k in val_dict[i]:
                    temp.append(j+k)
            res=temp
        return res
        
