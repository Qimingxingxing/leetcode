class Solution:
    def isValid(self, s: str) -> bool:
        arr = []
        
        d = {
            '}': '{',
            ']': '[',
            ')': '(',
        }
        
        # }]  : False
        for c in s:
            if c in d:
                if len(arr) == 0 or arr[-1] != d[c]:
                    return False
                else:
                    arr.pop()
            else:
                arr.append(c)
        
        return len(arr) == 0
