class Solution:
    def decodeString(self, s: str) -> str:
        st=[]
        cur_num=0
        cur_str=""
        for ch in s:
            if ch.isdigit():
                cur_num=cur_num*10+int(ch)
            elif ch=='[':
                st.append((cur_num,cur_str))
                cur_num=0
                cur_str=""
            elif ch==']':
                num1,prev=st.pop()
                cur_str=prev+num1*cur_str
            else:
                cur_str+=ch
        return cur_str
        
