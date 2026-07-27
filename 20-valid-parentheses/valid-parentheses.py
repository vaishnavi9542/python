class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        freq={']':'[','}':'{',')':'('}
        for ch in s:
            if ch in freq.values():
                st.append(ch)
            elif ch in freq.keys():
                if not st or st[-1]!=freq[ch]:
                    return False
                st.pop()
        return len(st)==0    