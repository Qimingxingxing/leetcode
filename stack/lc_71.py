class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        if not path: return ""
        q = path.split("/")
        ans = []
        for s in q:
            if s:
                if s == "..":
                    if ans:
                        ans.pop()
                elif s == ".":
                    continue
                else:
                    ans.append(s)
        return "/" + "/".join(ans)
