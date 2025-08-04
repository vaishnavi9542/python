class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        #num1=int(num1)
        #num2=int(num2)
        #return str(int(num1)*int(num2))
        if num1=="0" or num2=="0":
            return "0"
        def s(num):
            ans=0
            for i in num:
                ans=ans*10+(ord(i)-ord('0'))
            return ans
        def t(s):
            res=""
            while s:
                a=s%10
                s=s//10
                res=chr(ord('0')+a)+res
            return res
        return t(s(num1)*s(num2))
