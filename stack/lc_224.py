class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 5-(1+2)
        res = 0
        sign = 1
        stack = []
        i = 0
        while i< len(s):
            c = s[i]
            if c.isdigit():
                num = 0
                while i < len(s) and s[i] >= '0':
                    num = num *10 + int(s[i])
                    i += 1
                i -= 1
                res += sign * num
            elif c == "+":
                sign = 1
            elif c == "-":
                sign = -1
            elif c == "(":
                stack.append([res, sign])
                res = 0
                sign = 1
            elif c == ")":
                a, b = stack.pop()
                res = b*res + a
                sign = 1
            i+=1
        return res
        
