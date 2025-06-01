class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # (()) 4
        # (() 2
        # )()()) 4

        stack = [-1]
        res = 0
        for i, c in enumerate(s):
            if c == "(":
                stack.append(i)
            elif c == ")":
                idx = stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    res = max(res, i-stack[-1])
        return res
            
        

