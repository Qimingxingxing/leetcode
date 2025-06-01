class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 3-2*2+1
        st = []
        sign = "+"
        i = 0
        l = len(s)
        while i < l:
            if s[i].isdigit():
                j = i
                while j < l and s[j].isdigit():
                    j += 1
                num = int(s[i:j])
                i = j-1
            if i == l-1 or s[i] in ("+", "-", "*", "/"):
                if sign == "+":
                    st.append(num)
                elif sign == "-":
                    st.append(-num)
                elif sign == "*":
                    st.append(st.pop() * num)
                else:
                    st.append(int(float(st.pop()) / num))
                sign = s[i]            
            i += 1
        return sum(st)
