class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = len(s)
        stack = [[1, ""]]
        i = 0
        times = 1
        while i < l:
            if s[i].isdigit():
                j = i
                while j < l and s[j].isdigit():
                    j += 1
                times = int(s[i:j])
                i = j
            else:
                if s[i] == '[':
                    stack.append([times, ""])
                elif s[i] == ']':
                    a, b = stack.pop()
                    stack[-1][1] += a*b
                else:
                    stack[-1][1] += s[i]
                i += 1
        return stack[0][1]
