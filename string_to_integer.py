class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0
        result = ''
        nums = {'0','1','2','3','4','5','6','7','8','9'}  
        sign = 1
        i = 0
        if s[0] in ['+', '-']:
            if s[0] == '-':
                sign = -1
            i = 1  
        for char in s[i:]:
            if char in nums:
                result += char
            else:
                break
        if result == '':
            return 0
        result = result.lstrip('0')
        if result == '':
            return 0
        num = sign * int(result)
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        if num < INT_MIN:
            return INT_MIN
        if num > INT_MAX:
            return INT_MAX
        return num
