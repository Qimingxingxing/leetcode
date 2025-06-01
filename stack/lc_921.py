class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        # ()) = 1
        # (() = 1
        # )))((( = 6
        cnt = 0
        res = 0
        for c in s:
            if c == ")":
                if cnt == 0:
                    res += 1
                else:
                    cnt -= 1
            else:
                cnt += 1
        return cnt + res
