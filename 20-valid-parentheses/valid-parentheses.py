class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        freq={']':'[','}':'{',')':'('}
        for ch in s:
            if ch in freq.values():
                st.append(ch)
            elif ch in freq.keys():
                if not st or freq[ch]!=st.pop():
                    return False
        return not st        