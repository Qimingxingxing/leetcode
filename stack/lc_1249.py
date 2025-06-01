class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        right, stack = set(), []
        for i, c in enumerate(s):
            if c == "(":
                stack.append(i)
            elif c == ")":
                if not stack:
                    right.add(i)
                else:
                    stack.pop()
        res = ""
        for i, c in enumerate(s):
            if i not in set(stack) and i not in right:
                res += c
        return res
